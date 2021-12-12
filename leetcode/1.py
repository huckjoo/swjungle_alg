# 혼자 푼 풀이, 이분탐색을 적용해보고 싶었는데 실패
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pl = 0
        pr = len(nums)-1
        ans = []
        new_nums = []
        for idx, val in enumerate(nums):
            new_nums.append((val, idx))
        new_nums.sort()
        while pl < pr:
            if new_nums[pr][0] + new_nums[pl][0] > target:
                pr -= 1
            elif new_nums[pr][0] + new_nums[pl][0] < target:
                pl += 1
            else:
                ans.append(new_nums[pl][1])
                ans.append(new_nums[pr][1])
                break
        return ans
