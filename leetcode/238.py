# 혼자 푼 풀이
# Time Limit Exceeded O(N^2)
from typing import List


class Solution:
    def __init__(self) -> None:
        nums = [-1, 1, 0, -3, 3]
        self.productExceptSelf(nums)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        me = 0
        ans = []

        while me < len(nums):
            multiple = 1
            for i in range(len(nums)):
                if i == me:
                    continue
                multiple *= nums[i]
            ans.append(multiple)
            me += 1
        return ans


Solution()
