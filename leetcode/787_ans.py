from typing import List

from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))
        heap = [(0, src, K)]
        vis = [-1] * n  # K가 0인 경우가 있기 때문에 종료조건을 -1로 설정
        while heap:
            cost, node, k = heapq.heappop(heap)
            if node == dst:
                return cost
            if vis[node] >= k:  # k가 높아서 방문했던 곳이면 다시 가지 않음(가지치기)
                continue
            vis[node] = k
            for nxt_node, nxt_cost in graph[node]:
                heapq.heappush(heap, (cost+nxt_cost, nxt_node, k-1))
        return -1
