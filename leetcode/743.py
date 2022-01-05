from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))

        min_table = defaultdict(int)
        heap = [(0, k)]  # 시간, 시작점

        while heap:
            time, start_node = heapq.heappop(heap)
            if start_node not in min_table:
                min_table[start_node] = time
                for nxt_node, nxt_time in graph[start_node]:
                    heapq.heappush(heap, (nxt_time+time, nxt_node))

        if len(min_table) == n:
            return max(min_table.values())
        return -1
