import sys

n = int(sys.stdin.readline())
dp = [0] * 91
# bottom-up 방식
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

# top-down 방식
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if dp[n] != 0:
#         return dp[n]
#     else:
#         dp[n] = fibo(n-1) + fibo(n-2)
#         return dp[n]


# print(fibo(n))
