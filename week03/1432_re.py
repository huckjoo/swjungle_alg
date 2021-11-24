import sys
import heapq
n = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
degree = [0]*(n+1)
res = [0]*(n+1)
heap = []

for num in range(1, n+1):
    data = list(map(int, list(sys.stdin.readline().strip())))
    for idx, val in enumerate(data):
        if val == 1:
            graph[idx+1].append(num)
            degree[num] += 1

for num in range(1, n+1):
    if degree[num] == 0:
        heapq.heappush(heap, -num)

while heap:
    now = -heapq.heappop(heap)
    res[now] = n
    for x in graph[now]:
        degree[x] -= 1
        if degree[x] == 0:
            heapq.heappush(heap, -x)
    n -= 1

if res.count(0) > 1:
    print(-1)
else:
    print(*res[1:])
