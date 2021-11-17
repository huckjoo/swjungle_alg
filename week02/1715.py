import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))
total = 0
while len(heap) > 1:
    m1 = heapq.heappop(heap)
    m2 = heapq.heappop(heap)
    new = m1 + m2
    total += new
    heapq.heappush(heap, new)

print(total)
