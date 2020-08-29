# Google STEP 2020  Week1 Homework1  Review
# 普通のアナグラムを辞書から探して返すプログラム
# ハッシュテーブルを利用

from hash_table import HashTable
import time


# 辞書のデータファイルを読み込む関数
def read_dic(file):
    # 辞書データのファイルを読み込み、全て小文字に変換してリストdictionaryに格納
    with open(file) as f:
        dictionary = [s.strip().lower() for s in f]
    return dictionary


# ハッシュテーブルを作る関数
def make_hashmap(dictionary):
    hashmap = HashTable()
    for word in dictionary:
        hashmap.put(word)
    return hashmap


# アナグラムを見つける
def find_anagram_with_hashmap(word, hashmap):
    anagram_list = hashmap.get(word)
    return anagram_list


if __name__ == '__main__':
    dic_file = 'dictionary_words.txt'
    dictionary = read_dic(dic_file)
    hashmap = make_hashmap(dictionary)
    
    try:
        while True:
            word = input('input a word : ')
            ans_list = find_anagram_with_hashmap(word, hashmap)
            if len(ans_list) == 0:
                print('There is no anagram.')
            else:
                ans = ', '.join(ans_list)
                print(ans)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print('!!FINISH!!')