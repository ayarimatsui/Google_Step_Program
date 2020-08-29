# ハッシュテーブルの実装

class HashTable:

    def __init__(self):
        self.size = 0
        self.hashmap = [None] * 100000

    # ハッシュ関数
    def hash(self, key):
        p_dic = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
        idx = 0
        for k in key:
            idx *= (p_dic[k] % 100000)
            idx %= 100000
        return idx

    # ハッシュテーブルに(key, value)を入れる
    def put(self, key, value):
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            self.hashmap[idx] = [(key, value)]
        else:
            arr = self.hashmap[idx]
            for i in range(len(arr)):
                pair = arr[i]
                if pair[0] == key:
                    del arr[i]
                    break
            arr.append((key, value))
        self.size += 1

    # keyを元にハッシュテーブルに保持されているvalueの値を返す (ない時は-1を返す)
    def get(self, key):
        count = 1
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            return None
        else:
            arr = self.hashmap[idx]
            for i in range(len(arr)):
                pair = arr[i]
                if pair[0] == key:
                    return pair[1]
            return None

    # keyがハッシュテーブルの中にあるかどうかを調べる
    def contains(self, key):
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            return False
        else:
            arr = self.hashmap[idx]
            for i in range(len(arr)):
                pair = arr[i]
                if pair[0] == key:
                    return True
            return False

    # keyの要素をハッシュテーブルから削除
    def remove(self, key):
        idx = self.hash(key)
        arr = self.hashmap[idx]
        for i in range(len(arr)):
            pair = arr[i]
            if pair[0] == key:
                del arr[i]
                self.size -= 1
                break


