import bisect
import numpy as np

# ファイル'dictionary_words.txt'を読み込み、リストdictionaryに格納
with open('dictionary_words.txt') as f:
    dictionary = [s.strip() for s in f.readlines()]

def find_anagram(S):
    sorted_S = sorted(S)
    # 辞書の単語全てをソートした新しい辞書を作る
    new_dictionary = []
    for word in dictionary:
        # 全て小文字に変換
        word.lower()
        sorted_word = sorted(word)
        new_dictionary.append([sorted_word, word])
    new_dictionary.sort()

    # このあと列だけ取り出したいので、スライスで簡単に列だけ取り出せるndarrayに変換
    new_dictionary = np.array(new_dictionary)

    # ソートした結果が、sorted_Sと同じになるnew_dictionaryの単語のインデックスを取得
    # アナグラムが複数ある場合も考えられるので、同じ結果になる要素のインデックスの左端と右端の両方を取得しておく
    l = bisect.bisect_left(new_dictionary[:, 0], sorted_S)
    r = bisect.bisect_right(new_dictionary[:, 0], sorted_S)

    # ソートした結果が同じになる単語が、辞書から１つしか見つからずそれが引数と等しかった場合、または１つも見つからなっかった場合
    # = 元々の引数の文字列と同じもの以外、アナグラムが見つからなかった場合は、Noneを返す
    if (l - r == 1 and new_dictionary[l][1] == S) or l - r == 0:
        return None

    anagram_list = []
    for i in range(l, r):
        # 元の単語は答えに含まない
        if new_dictionary[i][1] != S:
            anagram_list.append(new_dictionary[i][1])

    return anagram_list

if __name__ == '__main__':
    # 標準入力
    S = input()
    # 全て小文字に変換
    S.lower()
    ans_list = find_anagram(S)
    if ans_list is None:
        print('There is no anagram')
    else:
        for word in ans_list:
            print(word)
