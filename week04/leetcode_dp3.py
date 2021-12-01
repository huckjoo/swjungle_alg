import sys


def rob(nums):
    N = len(nums)
    dp = [0]*(N)
    for i in range(N):
        dp[i] = nums[i]
    if N >= 3:
        for i in range(2, N):
            if i == 2:
                dp[i] = dp[i] + dp[i-2]
            elif i-3 >= 0:
                dp[i] = dp[i] + max(dp[i-2], dp[i-3])
    return max(dp)


nums = [2, 7, 9, 3, 1]
print(rob(nums))
