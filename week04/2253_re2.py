import sys

N, M = map(int, sys.stdin.readline().split())
small_stones = set()
for i in range(M):
    small_stones.add(int(sys.stdin.readline()))
max_v = int((2*N)**0.5)
dp = [[float('inf')]*(max_v + 2) for i in range(N+1)]

dp[1][0] = 0
# 2번 돌은 항상 점프가 가능하지 않다... 그래서 dp[2][1]로 놓고 풀면 틀린다.
for i in range(2, N+1):
    if i in small_stones:
        continue
    for v in range(1, max_v + 1):
        dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1
if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))
