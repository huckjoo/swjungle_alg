import sys

N, M = map(int, sys.stdin.readline().split())
board = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):        # 대소관계 표시
    a, b = map(int, sys.stdin.readline().split())
    board[a][b] = 1

for k in range(1, N+1):    # 연결
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][k] and board[k][j]:
                board[i][j] = 1

ans = 0
for i in range(1, N+1):  # 1부터 N까지 돌면서
    big = 0
    small = 0
    for j in range(1, N+1):
        if board[i][j] > 0:  # i입장에서 j보다 크다.
            small += 1
        if board[j][i] > 0:
            big += 1
    if big > N//2 or small > N//2:
        ans += 1
print(ans)
