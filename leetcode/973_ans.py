from typing import List
import heapq
'''
Runtime: 915 ms, faster than 29.16% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 20.7 MB, less than 10.89% of Python3 online submissions for K Closest Points to Origin.
'''
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y) # maxheap처럼 동작하게 해서 아래 heappushpop에서 max값을 빼주고 작은값들만 남기려 했다.
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y)) # 넣자마자 빼준다
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]