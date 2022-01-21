from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N < 3:
            for idx,val in enumerate(nums):
                if val == target:
                    return idx
            return -1
        l_start = 0
        l_end = nums.index(min(nums))-1
        if l_end < 0:
            for idx,val in enumerate(nums):
                if val == target:
                    return idx
        r_start = l_end+1
        r_end = N-1
        
        l = r = -1
        
        if target >= nums[l_start]:
            l = l_start
            r = l_end
        else:
            l = r_start
            r = r_end
        
        # 이분탐색 start
        while l<=r:
            mid = (r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1