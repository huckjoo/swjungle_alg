'''
Runtime: 1497 ms, faster than 14.45% of Python3 online submissions for Daily Temperatures.
Memory Usage: 25.3 MB, less than 68.77% of Python3 online submissions for Daily Temperatures.

어떤 값을 스택에 넣고, 언제 빼줘야 하는지 감이 잘 안온다...
'''
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for cur_day, cur_temp in enumerate(temperatures):
            while stack and cur_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                ans[prev_day] = cur_day - prev_day
            stack.append(cur_day)
        return ans
