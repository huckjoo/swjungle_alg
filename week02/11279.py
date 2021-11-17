import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, (-x, x))
    if x == 0:
        if len(heap) > 0:
            temp = heapq.heappop(heap)
            print(temp[1])
        else:
            print(0)
