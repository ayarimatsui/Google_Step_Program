# Google STEP 2020  Week1 Homework2  Review
# collections.Counterを使ってアナグラムを返すプログラム

import time
import collections

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
        word_count = collections.Counter(word)
        new_dic.append([word, word_count])
    return new_dic


# counterを使ってアナグラムを見つける
def find_anagram_with_counter(input_word, new_dictionary):
    input_count = collections.Counter(input_word)

    # 新しく作った辞書の単語について前から一つずつ調べていく
    anagram_list = []
    for word, word_count in new_dictionary:
        anagram = True
        for k, v in word_count.items():
            if input_count.get(k, 0) >= v:
                anagram = True
            else:
                anagram = False
                break
        if anagram and word != input_word:
            anagram_list.append(word)
    
    return anagram_list



if __name__ == '__main__':
    dic_file = 'dictionary_words.txt'
    dictionary = read_dic(dic_file)
    new_dic = make_new_dic(dictionary)

    try:
        while True:
            input_word = input('input a word : ')
            ans_list = find_anagram_with_counter(input_word, new_dic)
            if len(ans_list) == 0:
                print('There is no anagram.')
            else:
                ans = ', '.join(ans_list)
                print(ans)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print('!!FINISH!!')