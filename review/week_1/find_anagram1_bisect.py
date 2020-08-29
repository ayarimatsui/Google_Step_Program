# Google STEP 2020  Week1 Homework1  Review
# 普通のアナグラムを辞書から探して返すプログラム
# 二分探索を利用

import bisect
import time
from key_list import KeyList

# 辞書のデータファイルを読み込む関数
def read_dic(file):
    # 辞書データのファイルを読み込み、全て小文字に変換してリストdictionaryに格納
    with open(file) as f:
        dictionary = [s.strip().lower() for s in f]
    return dictionary


# 新しい辞書を作る関数
def make_new_dic(dictionary):
    new_dic = []
    for word in dictionary:
        new_dic.append([sorted(word), word])
    new_dic.sort()
    return new_dic


# 二分探索でアナグラムを見つける
def find_anagram_with_bisect(word, sorted_dic):
    sorted_word = sorted(word)
    # ソート済の辞書に対して二分探索
    left = bisect.bisect_left(KeyList(sorted_dic, key=lambda x: x[0]), sorted_word)
    right = bisect.bisect_right(KeyList(sorted_dic, key=lambda x: x[0]), sorted_word)

    # 元々の単語は除外して、アナグラムのリストを作って返す
    anagram_list = []
    for _, anagram_word in sorted_dic[left:right]:
        if anagram_word != word:
            anagram_list.append(anagram_word)
    
    return anagram_list


if __name__ == '__main__':
    dic_file = 'dictionary_words.txt'
    dictionary = read_dic(dic_file)
    sorted_dic = make_new_dic(dictionary)
    print(len(dictionary))

    try:
        while True:
            word = input('input a word : ')
            ans_list = find_anagram_with_bisect(word, sorted_dic)
            if len(ans_list) == 0:
                print('There is no anagram.')
            else:
                ans = ', '.join(ans_list)
                print(ans)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print('!!FINISH!!')
    