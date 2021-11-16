import sys
import heapq

n = int(sys.stdin.readline())
left = []  # maxheap으로 구성
right = []  # minheap으로 구성
for i in range(n):
    num = int(sys.stdin.readline())
    if len(left) > len(right):
        heapq.heappush(right, (num, num))
    else:
        heapq.heappush(left, (-num, num))
    if len(left) > 0 and len(right) > 0:
        if left[0][1] > right[0][1]:  # 만약 왼쪽 최대값이 오른쪽 최소값보다 크다면
            l1 = heapq.heappop(left)  # 튜플을 뽑아와서 변수에 대입할수가 없을 수 있음
            r1 = heapq.heappop(right)
            heapq.heappush(right, (l1[1], l1[1]))
            heapq.heappush(left, (-r1[1], r1[1]))
    print(left[0][1])
