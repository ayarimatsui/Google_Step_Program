# Homework2の発展課題
# i can haz wordz で高得点取れる文字列を返すプログラム

import collections

# ファイル'dictionary_words.txt'を読み込み、 全て大文字にしてリストdictionaryに格納
with open('dictionary_words.txt') as f:
    dictionary = [s.strip().upper() for s in f.readlines()]

def find_word(input_str):
    # 各文字がいくつずつあるのか辞書にまとめる
    input_count = collections.Counter(input_str)
    # 辞書中の各単語ごとに、各文字がいくつずつあるのか数えて、新しい辞書を作る
    new_dictionary = []
    for word in dictionary:
        word_count = collections.Counter(word)
        new_dictionary.append([word, word_count])

    best_word = None
    best_score = 0
    # 新しく作った辞書の単語について前から一つずつ調べていく
    for i in range(len(new_dictionary)):
        flag = True
        '''辞書中の単語が引数の文字列に使われている文字しか使っておらず、かつそれぞれの文字の登場回数が
        　　元々の文字列以下の時のみ、flag = True のままになるようにする
        '''
        for k, v in new_dictionary[i][1].items():
            if (k not in input_count.keys()) or (v > input_count[k]):
                flag = False
                break
        if flag:
            # 得点を計算する
            score = 0
            for j in range(len(new_dictionary[i][0])):
                if new_dictionary[i][0][j] in ['A', 'B', 'D', 'E', 'G', 'I', 'N', 'O', 'R', 'S', 'T', 'U']:
                    score += 1
                    # j - 1文字目が'Q', j文字目が'U'の時は'U'で足してしまった1をscoreから引く
                    if j > 0:
                        if [new_dictionary[i][0][j - 1], new_dictionary[i][0][j]] == ['Q', 'U']:
                            score -= 1
                elif new_dictionary[i][0][j] in ['C', 'F', 'H', 'L', 'M', 'P', 'V', 'W', 'Y']:
                    score += 2
                else:
                    score += 3
            score = (score + 1) ** 2
            if score > best_score:
                best_score = score
                best_word = new_dictionary[i][0]

    return best_score, best_word

if __name__ == '__main__':
    # 標準入力
    '''
    入力はとりあえず、下のような形ということにしています(コピぺしたらちょうどこの形式になっていたので)
    A
    D
    B
    Qu
    C
    F
    G ...
    '''
    for _ in range(10):
        input_list = [input().upper() for _ in range(16)]
        # 'Qu'をばらけさせたいので、文字列に変換
        input_str = ''.join(input_list)
        best_score, best_word = find_word(input_str)
        if best_word is None:
            print('PASS')
        else:
            print(best_word)
            print(best_score)
