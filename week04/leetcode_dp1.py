def maxSubArray(nums):
    length = len(nums)
    dp = [0]*length
    dp[0] = nums[0]
    for i in range(1, length):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    return max(dp)


nums = [5, 4, -1, 7, 8]
print(maxSubArray(nums))
