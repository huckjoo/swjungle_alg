from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0
        ans = []
        prev_nums = []

        def dfs(nums, start, total):
            # 종료조건
            if total == target:
                if len(prev_nums) > 0:
                    ans.append(prev_nums[:])
            if total > target:
                return
            for num in nums:
                if num >= start:
                    total += num
                    prev_nums.append(num)
                    dfs(nums, num, total)
                    prev_nums.pop()
                    total -= num
        candidates = sorted(candidates)
        dfs(candidates, candidates[0], 0)
        return ans
