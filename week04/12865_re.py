import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0]*(K+1) for i in range(N+1)]
things = [[0, 0]]

for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    things.append([w, v])

for y in range(1, N+1):
    weight = things[y][0]
    val = things[y][1]
    for x in range(K+1):
        if x-weight >= 0:
            dp[y][x] = max(dp[y-1][x], dp[y-1][x-weight] + val)
        else:
            dp[y][x] = dp[y-1][x]

print(dp[N][K])
