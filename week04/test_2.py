import sys
print(float(0.1 + 0.2))
sys.setrecursionlimit(10**6)
M, N = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[0]*N for _ in range(M)]
dp = [[-1]*N for _ in range(M)]


def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1
    if dp[y][x] != -1:  # 메모이제이션
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N:  # 갈 수 있음
            if board[y][x] > board[ny][nx]:
                dp[y][x] += dfs(ny, nx)
    return dp[y][x]


print(dfs(0, 0))
