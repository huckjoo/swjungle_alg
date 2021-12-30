from typing import List

# Runtime: 79 ms, faster than 5.45% of Python3 online submissions for Subsets.
# Memory Usage: 14.4 MB, less than 79.30% of Python3 online submissions for Subsets.


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        start = nums[0]-1
        prev_nums = []

        def dfs(nums, start):
            for num in nums:
                if num > start:
                    prev_nums.append(num)
                    ans.append(prev_nums[:])
                    start = num
                    dfs(nums, start)
                    prev_nums.pop()
        dfs(nums, start)
        ans.append([])
        return ans
