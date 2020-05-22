# Google_Step_Program/week_2/homework1
# 行列積を求めるプログラム  Numpy バージョン
# csvファイルにNに対してかかった実行時間を保存していく

import numpy, sys, time
import csv

file = open('matrix_numpy.csv', 'w')
w = csv.writer(file)

for n in range(2, 100):
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i

    begin = time.time()

    c = numpy.dot(a, b)

    end = time.time()

    record = end - begin
    w.writerow([n, record])

file.close()
print('done')
