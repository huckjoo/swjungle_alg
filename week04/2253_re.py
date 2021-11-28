import sys

n, m = map(int, sys.stdin.readline().split())
small_stones = set()
for _ in range(m):
    small_stones.add(int(sys.stdin.readline()))
INF = float('inf')
max_v = int((2*n)**0.5) + 1
dp = [[INF]*(max_v+1) for i in range(n+1)]

dp[2][1] = 1

for i in range(3, n+1):
    if i in small_stones:
        continue
    for v in range(1, max_v):
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1])+1

if min(dp[n]) == INF:
    print(-1)
else:
    print(min(dp[n]))
