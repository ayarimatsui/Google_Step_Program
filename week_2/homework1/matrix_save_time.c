// Google_Step_Program/week_2/homework1
// 行列積を求めるプログラム  C バージョン
// csvファイルにNに対してかかった実行時間を保存していく

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

double get_time()
{
  struct timeval tv;
  gettimeofday(&tv, NULL);
  return tv.tv_sec + tv.tv_usec * 1e-6;
}

int main(int argc, char** argv)
{
  FILE *fp;
  char *fname = "matrix_c.csv";

  fp = fopen(fname, "w");
  if( fp == NULL ){
    printf( "%sファイルが開けません\n", fname );
    return -1;
  }

  int n;

  for (n = 2; n < 100; n++) {
    double* a = (double*)malloc(n * n * sizeof(double)); // Matrix A
    double* b = (double*)malloc(n * n * sizeof(double)); // Matrix B
    double* c = (double*)malloc(n * n * sizeof(double)); // Matrix C

    // Initialize the matrices to some values.
    int i, j;
    for (i = 0; i < n; i++) {
      for (j = 0; j < n; j++) {
        a[i * n + j] = i * n + j; // A[i][j]
        b[i * n + j] = j * n + i; // B[i][j]
        c[i * n + j] = 0; // C[i][j]
      }
    }

    double begin = get_time();

    int row, col;
    for (row = 0; row < n; row++) {
      for (col = 0; col < n; col++) {
        for (i = 0; i < n; i ++) {
          c[row * n + col] += a[row * n + i] * b[i * n + col];
        }
      }
    }

    double end = get_time();
    fprintf(fp, "%d, %f\n", n, end - begin);

    free(a);
    free(b);
    free(c);
  }
  printf("done\n");
  return 0;
}
