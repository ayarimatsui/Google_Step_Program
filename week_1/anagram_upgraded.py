import collections

# ファイル'dictionary_words.txt'を読み込み、リストdictionaryに格納
with open('dictionary_words.txt') as f:
    dictionary = [s.strip() for s in f.readlines()]

def find_anagram_upgraded(S):
    # 各文字がいくつずつあるのか辞書にまとめる
    S_count = collections.Counter(S)
    # 辞書中の各単語ごとに、各文字がいくつずつあるのか数えて、新しい辞書を作る
    new_dictionary = []
    for word in dictionary:
        # 全て小文字に変換
        word.lower()
        word_count = collections.Counter(word)
        new_dictionary.append([word, word_count])

    anagram_list = []
    # 新しく作った辞書の単語について前から一つずつ調べていく
    for i in range(len(new_dictionary)):
        flag = True
        '''辞書中の単語が引数の文字列に使われている文字しか使っておらず、かつそれぞれの文字の登場回数が
        　　元々の文字列以下の時のみ、flag = True のままになるようにする
        '''
        for k, v in new_dictionary[i][1].items():
            if (k not in S_count.keys()) or (v > S_count[k]):
                flag = False
                break
        if flag and new_dictionary[i][0] != S:
            anagram_list.append(new_dictionary[i][0])

    return anagram_list

if __name__ == '__main__':
    # 標準入力
    S = input()
    # 全て小文字に変換
    S.lower()
    ans_list = find_anagram_upgraded(S)
    if len(ans_list) == 0:
        print('There is no anagram')
    else:
        for word in ans_list:
            print(word)
