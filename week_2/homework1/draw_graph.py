# matrix_python.csv, matrix_numpy.csv, matrix_c.csvに保存したデータを読み込み、グラフを描く
# 行列の積を求めるプログラムの実行時間を、Python, Numpy, Cで比較する
import csv
import matplotlib.pyplot as plt
import numpy as np

python_file = open('matrix_python.csv', 'r')
reader1 = csv.reader(python_file)
python_time = [float(row[1]) for row in reader1]
python_file.close()

numpy_file = open('matrix_numpy.csv', 'r')
reader2 = csv.reader(numpy_file)
numpy_time = [float(row[1]) for row in reader2]
numpy_file.close()

c_file = open('matrix_c.csv', 'r')
reader3 = csv.reader(c_file)
c_time = [float(row[1]) for row in reader3]
c_file.close()

x = list(range(2, 100))

# グラフの描画
plt.plot(x, python_time, label="Python")
plt.plot(x, numpy_time, label="Numpy")
plt.plot(x, c_time, label="C")
plt.title("Execution Time")
plt.xlabel("size of N")
plt.ylabel("time (s)")
plt.legend(loc="best")
plt.show()
