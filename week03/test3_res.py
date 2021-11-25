import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([end, weight])
    graph[end].append([start, weight])

start_island, end_island = map(int, sys.stdin.readline().split())

min_weight, max_weight = 1, 1000000000


def BFS(mid_weight):
    queue = deque()
    queue.append(start_island)
    visited = set()
    visited.add(start_island)
    while queue:
        start = queue.popleft()
        for end, weight in graph[start]:
            if end not in visited and weight >= mid_weight:
                visited.add(end)
                queue.append(end)

    if end_island in visited:
        return True
    else:
        return False


result = min_weight
while min_weight <= max_weight:
    mid_weight = (min_weight + max_weight) // 2
    if BFS(mid_weight):
        result = mid_weight
        min_weight = mid_weight + 1
    else:
        max_weight = mid_weight - 1

print(result)
