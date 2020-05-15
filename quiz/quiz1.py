# 過半数を占めるものがある時、O(1)のメモリを使ってその値を当てる方法

import sys
def judge_majority():
    count = 0
    cand = None
    while True:
        n = sys.stdin.readline()[:-1] # 改行コードを取り除いて入力を取得
        if str.isdecimal(n):  # 入力が数字に変換可能かどうかを確かめる
            num = int(n)
            if count == 0:
                cand = num
            if num == cand:
                count += 1
            else:
                count -= 1
        else:  # 入力が数字に変換できない時、つまり数字が流れてくるのが終わった時、ループから抜ける
            break
    return cand
ans = judge_majority()
print(ans)

'''
(入力例)
1
4
5
5
5
10
5
10
2
5
5
5
'''
