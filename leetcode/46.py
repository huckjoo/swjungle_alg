from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        prev_nums = []

        def dfs(nums):
            # 종료조건
            if len(nums) == 0:
                # [:]을 빼면 안되는데 이유는? -> 참조관계를 가져서 값이 변경됨 따라서 copy()나 [:]를 써야함
                ans.append(prev_nums[:])
            # 실행과정
            for num in nums:
                curr_nums = nums[:]  # [:]을 빼면 안되는데 이유는?
                curr_nums.remove(num)
                prev_nums.append(num)
                # 재귀과정
                dfs(curr_nums)
                prev_nums.pop()
        dfs(nums)
        return ans
