# ハッシュテーブルの実装
# 衝突した時はオープンアドレス法で衝突を回避

class HashTable:

    def __init__(self, N):  # Nはハッシュテーブルのサイズ
        self.size = N
        self.hashmap = [None] * self.size

    # ハッシュ関数
    def hash(self, key):
        idx = 0
        for k in key:
            idx += (ord(k) % self.size)
            idx %= self.size
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

    # keyを元にハッシュテーブルに保持されているvalueの値を返す (ない時は-1を返す)
    def get(self, key):
        count = 1
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            return -1
        else:
            arr = self.hashmap[idx]
            for i in range(len(arr)):
                pair = arr[i]
                if pair[0] == key:
                    return pair[1]
            return -1

    # keyがハッシュテーブルの中にあるかどうかを調べる
    def contains(self, key):
        idx = self.hash(key)
        if self.hashmap[idx] is None:
            return None
        else:
            arr = self.hashmap[idx]
            for i in range(len(arr)):
                pair = arr[i]
                if pair[0] == key:
                    return True
            return False

    # keyの要素をハッシュテーブルから削除
    def remove(self, key):
        if not self.contains(key):
            return
        else:
            idx = self.hash(key)
            arr = self.hashmap[idx]
            for i in range(len(arr)):
                pair = arr[i]
                if pair[0] == key:
                    del arr[i]
                    break
