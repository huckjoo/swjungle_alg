
from typing import List
'''
Runtime: 1285 ms, faster than 12.95% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 20.5 MB, less than 15.81% of Python3 online submissions for K Closest Points to Origin.
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        ans = []
        for point in points:
            x = point[0]
            y = point[1]
            temp = [(x**2 + y**2),x,y]
            arr.append(temp)
            
        arr.sort(key=lambda x:x[0])
        
        for tmp in arr[:k]:
            ans.append([tmp[1],tmp[2]])
        return ans
        