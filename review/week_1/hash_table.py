# ハッシュテーブルの実装

class HashTable:

    def __init__(self):
        self.size = 0
        self.hashmap = [None] * 1000000

    # ハッシュ関数
    def hash(self, word):
        p_dic = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
        idx = 1
        for s in word:
            idx *= p_dic[s]
            idx %= 1000000
        return idx

    # ハッシュテーブルにwordを入れる
    def put(self, word):
        idx = self.hash(word)
        if self.hashmap[idx] is None:
            self.hashmap[idx] = [word]
        else:
            lst = self.hashmap[idx]
            lst.append(word)
            self.hashmap[idx] = lst
        self.size += 1

    # idxを元にハッシュテーブルに保持されている単語のリストを返す (ない時は空リストを返す)
    def get(self, word):
        count = 1
        idx = self.hash(word)
        if self.hashmap[idx] is None:
            return []
        else:
            lst = self.hashmap[idx]
            anagram_lst = []
            for elem in lst:
                if elem != word:
                    anagram_lst.append(elem)
            return anagram_lst



