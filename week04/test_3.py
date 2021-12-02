import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jewels = []  # N: 보석 개수
bags = []   # K: 가방 개수
for _ in range(N):  # 보석 정보 저장
    jewels.append(list(map(int, sys.stdin.readline().split())))
for _ in range(K):  # 가방의 최대무게 저장
    bags.append(int(sys.stdin.readline()))

jewels.sort()  # 보석은 가장 가벼운 순으로 저장한다.
bags.sort()  # 가방은 작은 순서대로 정렬
heap = []
ans = 0
temp = []
for bag in bags:  # 작은 가방 순서대로 뽑아서
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(temp, -jewels[0][1])  # 값을 temp에 넣어줌
        heapq.heappop(jewels)
    if temp:
        ans += -heapq.heappop(temp)
print(ans)
