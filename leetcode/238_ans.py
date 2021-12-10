# discuss 풀이
# Time O(N) Space O(1)
# 이런 기술은 어떻게 생각하는것인가...
from typing import List


class Solution:
    def __init__(self) -> None:
        nums = [-1, 1, 0, -3, 3]
        self.productExceptSelf(nums)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        p = 1
        for i in range(0, length):
            ans.append(p)
            p = p*nums[i]
        p = 1
        for i in range(length-1, -1, -1):
            ans[i] = ans[i]*p
            p = p*nums[i]
        return ans


Solution()
