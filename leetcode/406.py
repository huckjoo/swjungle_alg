from typing import List
import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        result = []
        for person in people:
            heapq.heappush(heap,[-person[0],person[1]])
        
        while heap:
            now = heapq.heappop(heap)
            result.insert(now[1],[-now[0],now[1]])
        return result