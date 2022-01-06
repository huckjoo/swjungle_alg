from collections import defaultdict
import heapq
from typing import List

# TLE 코드


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))

        heap = [(0, src, 0)]  # cost,start,cnt
        while heap:
            cost, node, cnt = heapq.heappop(heap)
            if node == dst:
                return cost
            if cnt <= k:
                cnt += 1
                for nxt_node, nxt_cost in graph[node]:
                    total_cost = nxt_cost + cost
                    heapq.heappush(heap, (total_cost, nxt_node, cnt))

        return -1
