import sys
n, b = map(int, sys.stdin.readline().split())
A = [[0]*n for _ in range(n)]
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        A[i][j] = tmp[j]


def matrix_mult(A, b):
    # 앞의 행렬의 행, 뒤의 행렬의 열로 전체 틀이 갖춰진다.
    temp = [[0]*n for _ in range(n)]
    if b == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= 1000
        return A
    elif b % 2 != 0:  # B가 홀수면
        matrix_div = matrix_mult(A, b-1)
        for i in range(n):  # i는 앞의 행렬의 행 개수
            for j in range(n):  # j는 앞의 행렬의 열 개수
                for k in range(n):
                    temp[i][j] += matrix_div[i][k] * A[k][j]
                temp[i][j] %= 1000
        return temp
    elif b % 2 == 0:  # B가 짝수면
        matrix_div = matrix_mult(A, b//2)
        for i in range(n):  # i는 앞의 행렬의 행 개수
            for j in range(n):  # j는 앞의 행렬의 열 개수
                for k in range(n):
                    temp[i][j] += matrix_div[i][k] * matrix_div[k][j]
                temp[i][j] %= 1000
        return temp


ans = matrix_mult(A, b)
for i in range(n):
    for j in range(n):
        print(ans[i][j], end=' ')
    print()
