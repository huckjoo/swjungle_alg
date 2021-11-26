import sys

N, K = map(int, sys.stdin.readline().split())

things = [(0, 0)]

for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    things.append((w, v))

board = [[0]*(K+1) for i in range(N+1)]

for i in range(1, N+1):
    weight = things[i][0]
    val = things[i][1]
    for j in range(1, K+1):
        if j-weight >= 0:
            board[i][j] = max(board[i-1][j], board[i-1][j-weight]+val)
        else:
            board[i][j] = board[i-1][j]  # 얘가 없으면 틀렸다고 나옴 -> 앞선 결과를 받아오지 못해서

print(board[N][K])
