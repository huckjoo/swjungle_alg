# dp로 풀어보자.
import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
dp = [0] + [100001 for i in range(k)]
for i in range(n):
    coins.append(int(sys.stdin.readline()))
for c in coins:
    for i in range(1, k+1):
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)
    print(dp)
