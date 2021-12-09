# 혼자 푼 풀이
# fail
from typing import List


class Solution:
    def __init__(self) -> None:
        nums = []
        self.threeSum(nums)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sorted_nums = sorted(nums)
        zero_idx = sorted_nums.index(0)
        # case 0 - [0,0,0]
        cnt_zero = 0
        for i in range(zero_idx):
            if sorted_nums[i] == 0:
                cnt_zero += 1
        if cnt_zero >= 3:
            ans.append([0, 0, 0])
        # case 1 - 1개 0(1개) 1개
        p_center = zero_idx
        p_right = zero_idx + 1
        p_left = zero_idx - 1
        # sorted_nums = [-4,-1,-1,0,1,2]
        while p_right < len(sorted_nums) and p_left >= 0:
            if sorted_nums[p_left] + sorted_nums[p_right] == 0:
                ans.append([sorted_nums[p_left], 0, sorted_nums[p_right]])
            p_right += 1
            p_left -= 1
        # case 2 - 2개 0 1개
        for left_one in range(0, zero_idx):
            for left_two in range(left_one+1, zero_idx):
                for right_three in range(zero_idx+1, len(sorted_nums)):
                    if (sorted_nums[left_one] + sorted_nums[left_two] + sorted_nums[right_three] == 0):
                        ans.append(
                            [sorted_nums[left_one], sorted_nums[left_two], sorted_nums[right_three]])
                        break
        # case 3 - 1개 0 2개
        for left_one in range(0, zero_idx):
            for right_two in range(zero_idx+1, len(sorted_nums)):
                for right_three in range(right_two+1, len(sorted_nums)):
                    if (sorted_nums[left_one] + sorted_nums[right_two] + sorted_nums[right_three] == 0):
                        ans.append(
                            [sorted_nums[left_one], sorted_nums[right_two], sorted_nums[right_three]])
                        break
        print(ans)
        return


Solution()
