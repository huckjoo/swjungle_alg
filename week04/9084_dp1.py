import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0]*10001
    for coin in coins:
        dp[coin] = coin
        for i in range(coin, N+1):
            dp[i] = dp[i-coin] + 1
