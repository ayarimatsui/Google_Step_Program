# Google STEP Program  week2 homework4

import sys
from hashmap import HashTable   # hashmap.pyより定義したHashTableをimportする

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.

# url, contents, 前後に追加されたデータを記録しておくオブジェクト
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class Cache:
  # Initializes the cache.
  # |n|: The size of the cache.
  def __init__(self, n):
    self.size = n
    self.hashmap = HashTable()
    # 現在ハッシュテーブルに保存されているものの中で一番古いもの
    self.head = Node(None, None)
    # 現在ハッシュテーブルに保存されているものの中で一番新しいもの
    self.tail = Node(None, None)
    self.head.next = self.tail
    self.tail.prev = self.head

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # |url|: The accessed URL
  # |contents|: The contents of the URL
  def access_page(self, url, contents):
    node = Node(url, contents)
    # 新しくハッシュテーブルに入れたいurlがすでにハッシュテーブルにある時
    if self.hashmap.contains(url):
        # 元々ハッシュテーブルに保存されていたノードを取り出す
        old_node = self.hashmap.get(url)
        self.hashmap.remove(url)
        if old_node == self.head:
            self.head = self.head.next
        elif old_node == self.tail:
            self.tail = self.tail.prev
        else:
            # 削除したノードの前後にあったノードの前後情報を修正
            old_node_prev = old_node.prev
            old_node_next = old_node.next
            old_node_prev.next = old_node_next
            old_node_next.prev = old_node_prev
        # 新しいものをハッシュテーブルに保存し、一番後ろのノードに付け加える
        self.hashmap.put(url, node)
        old_tail = self.tail
        old_tail.next = node
        self.tail = node
        self.tail.prev = old_tail

    else:
        if self.head.key is None:
            self.hashmap.put(url, node)
            self.head = self.head.next
            old_tail = self.tail
            old_tail.next = node
            self.tail = node
            self.tail.prev = old_tail
        else:
            # ハッシュテーブルがすでにn個のデータを保存している時
            if self.hashmap.size >= self.size:
                # ハッシュテーブルの中で一番古いurlを取り出す
                key_to_delete = self.head.key
                self.hashmap.remove(key_to_delete)
                self.head = self.head.next
            self.hashmap.put(url, node)
            old_tail = self.tail
            old_tail.next = node
            self.tail = node
            self.tail.prev = old_tail

  # Return the URLs stored in the cache. The URLs are ordered
  # in the order in which the URLs are mostly recently accessed.
  def get_pages(self):
    pages_list = []
    cur_node = self.head
    if cur_node.key is not None:
        pages_list.append(cur_node.key)
    while cur_node.next:
        cur_node = cur_node.next
        if cur_node.key is not None:
            pages_list.append(cur_node.key)
    pages_list.reverse()
    return pages_list


# Does your code pass all test cases? :)
def cache_test():
  # Set the size of the cache to 4.
  cache = Cache(4)
  # Initially, no page is cached.
  #print(cache.get_pages())
  equal(cache.get_pages(), [])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # "a.com" is cached.
  #print(cache.get_pages())
  equal(cache.get_pages(), ["a.com"])
  # Access "b.com".
  cache.access_page("b.com", "BBB")
  # The cache is updated to:
  #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
  #print(cache.get_pages())
  equal(cache.get_pages(), ["b.com", "a.com"])
  # Access "c.com".
  cache.access_page("c.com", "CCC")
  # The cache is updated to:
  #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
  #print(cache.get_pages())
  equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
  # Access "d.com".
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  #print(cache.get_pages())
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "d.com" again.
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  #print(cache.get_pages())
  equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
  # Access "a.com" again.
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
  #print(cache.get_pages())
  equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
  cache.access_page("c.com", "CCC")
  #print(cache.get_pages())
  equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  #print(cache.get_pages())
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  cache.access_page("a.com", "AAA")
  #print(cache.get_pages())
  equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is full, so we need to remove the least recently accessed page "b.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
  #print(cache.get_pages())
  equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
  # Access "f.com".
  cache.access_page("f.com", "FFF")
  # The cache is full, so we need to remove the least recently accessed page "c.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
  #print(cache.get_pages())
  equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
  print("OK!")

# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
  assert(list1 == list2)
  for i in range(len(list1)):
    assert(list1[i] == list2[i])

if __name__ == "__main__":
  cache_test()
