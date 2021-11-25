
dp = [0]*100  # 99개까지의 인덱스 구현가능


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if dp[x] != 0:
        return dp[x]
    else:
        dp[x] = fibo(x-1) + fibo(x-2)
        return dp[x]


print(fibo(99))
