t = int(input())
for i in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0 for i in range(m + 1)]
    dp[0] = 1    # 2원으로 2원을 만드는 경우 -> 1번은 만들 수 있기 때문에 dp[0]=1로 저장
    for coin in coins:
        for j in range(1, m + 1):
            if j - coin >= 0:  # j가 coin보다 크거나 같을 때만 고려해도 됨. 예를 들면 5원으로 1,2,3,4원을 만들 수 없기 때문임
                dp[j] += dp[j - coin]
    print(dp[m])
