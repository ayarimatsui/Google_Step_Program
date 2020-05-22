# Google_Step_Program/week_2/homework1
# 行列積を求めるプログラム  Python バージョン
# csvファイルにNに対してかかった実行時間を保存していく

import numpy, sys, time
import csv

file = open('matrix_python.csv', 'w')
w = csv.writer(file)

for n in range(2, 100):
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    for row in range(n):
        for col in range(n):
            c[row][col] = sum([a[row][i] * b[i][col] for i in range(n)])
            #for i in range(n):
                #c[row][col] += a[row][i] * b[i][col]

    end = time.time()
    record = end - begin
    w.writerow([n, record])

file.close()
print('done')
