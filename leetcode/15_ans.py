class Solution:
    def __init__(self) -> None:
        nums = [-4, -1, -1, -1, -1, 0, 1, 2]
        self.threeSum(nums)

    def threeSum(self, nums):
        ans = []
        nums = sorted(nums)
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p_left = i+1
            p_right = len(nums)-1
            while p_left < p_right:
                now_sum = nums[i] + nums[p_left] + nums[p_right]
                if now_sum > 0:
                    p_right -= 1
                elif now_sum < 0:
                    p_left += 1
                else:
                    ans.append([nums[i], nums[p_left], nums[p_right]])
                    while p_left < p_right and nums[p_left] == nums[p_left+1]:
                        p_left += 1
                    while p_left < p_right and nums[p_right] == nums[p_right-1]:
                        p_right -= 1
                    p_left += 1
                    p_right -= 1
        return ans


Solution()
