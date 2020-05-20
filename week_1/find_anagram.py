# Homework 1

import bisect

# ファイル'dictionary_words.txt'を読み込み、全て小文字に変換してリストdictionaryに格納
with open('dictionary_words.txt') as f:
    dictionary = [s.strip().lower() for s in f]

class KeyList(object):
    # bisect doesn't accept a key function, so we build the key into our sequence.
    def __init__(self, l, key):
        self.l = l
        self.key = key
    def __len__(self):
        return len(self.l)
    def __getitem__(self, index):
        return self.key(self.l[index])

def find_anagram(S):
    sorted_S = sorted(S)
    # 辞書の単語全てをソートした新しい辞書を作る
    new_dictionary = []
    for word in dictionary:
        sorted_word = sorted(word)
        new_dictionary.append([sorted_word, word])
    new_dictionary.sort()

    # ソートした結果が、sorted_Sと同じになるnew_dictionaryの単語のインデックスを取得
    # アナグラムが複数ある場合も考えられるので、同じ結果になる要素のインデックスの左端と右端の両方を取得しておく
    left = bisect.bisect_left(KeyList(new_dictionary, key=lambda x: x[0]), sorted_S)
    right = bisect.bisect_right(KeyList(new_dictionary, key=lambda x: x[0]), sorted_S)

    anagram_list = []
    for _, target in new_dictionary[left:right]:
        # 元の単語は答えに含まない
        if target != S:
            anagram_list.append(target)

    return anagram_list

if __name__ == '__main__':
    # 標準入力
    S = input()
    # 全て小文字に変換
    S = S.lower()
    ans_list = find_anagram(S)
    if len(ans_list) == 0:
        print('There is no anagram')
    else:
        for word in ans_list:
            print(word)
