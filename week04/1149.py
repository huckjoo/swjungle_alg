import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*3 for i in range(N)]


for i in range(3):
    dp[0][i] = board[0][i]
for row in range(1, N):
    dp[row][0] = board[row][0] + min(dp[row-1][1], dp[row-1][2])
    dp[row][1] = board[row][1] + min(dp[row-1][0], dp[row-1][2])
    dp[row][2] = board[row][2] + min(dp[row-1][0], dp[row-1][1])

print(min(dp[N-1]))
