import sys
N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*(N) for i in range(N)]

for i in range(1, N):
    for j in range(0, N-i):
        if i == 1:
            dp[j][i+j] = matrix[j][0]*matrix[j][1]*matrix[i+j][1]
            continue
        dp[j][i+j] = 2**32
        for k in range(j, i+j):
            dp[j][i+j] = min(dp[j][i+j], dp[j][k]+dp[k+1][j+i] +
                             matrix[j][0]*matrix[k][1]*matrix[i+j][1])
print(dp[0][N-1])
