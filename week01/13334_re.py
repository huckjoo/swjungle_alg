import sys
import heapq

n = int(sys.stdin.readline())
row_data = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    row_data.append([a, b])

L = int(sys.stdin.readline())

roads = []
for x in row_data:
    if x[1]-x[0] <= L:
        roads.append(x)
roads.sort(key=lambda x: x[1])

heap = []
ans = [0]
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1]-L:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    ans.append(len(heap))
print(max(ans))
