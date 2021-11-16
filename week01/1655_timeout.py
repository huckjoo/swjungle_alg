# 시간초과 나는 코드 > 왜? N이 100000개인데 시간복잡도가 O(N^2)를 따르기 때문으로 보임
import sys
import heapq

n = int(sys.stdin.readline())
data = []
for i in range(n):
    x = int(sys.stdin.readline())
    data.append(x)
k = 0
while k < n:
    heap = []
    num = k+1
    for i in range(k+1):
        heapq.heappush(heap, data[i])
    t = 0
    if num % 2 == 0:
        t = num//2-1
    else:
        t = num//2
    backup = []
    for _ in range(t):  # 반만 pop한다.
        tmp = heapq.heappop(heap)
        backup.append(tmp)
    # print('backup:', backup)
    print(heap[0])
    for x in backup:  # pop한놈들 다시 넣어준다.
        heapq.heappush(heap, x)
    # print('heap:', heap)
    k += 1
