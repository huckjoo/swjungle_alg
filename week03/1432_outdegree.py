# 뒤집었을 경우
import sys
import heapq


def topology_sort(N):
    heap = []
    for num in range(1, N + 1):
        # 뒤집은 상태에서 indegree를 본다. indegree가 0인 것부터 우선순위 큐에 넣는다. 높은 숫자부터 보기 위해 max heap사용
        if degree[num] == 0:
            heapq.heappush(heap, -num)

    while heap:
        now = -heapq.heappop(heap)
        result[now] = N          # N부터 하나씩 빼주면서 now에 바꿔준다.
        for adj_num in graph[now]:
            degree[adj_num] -= 1
            if degree[adj_num] == 0:
                heapq.heappush(heap, -adj_num)
        N -= 1


N = int(sys.stdin.readline())

degree = [0] * (N + 1)
result = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for num in range(1, N + 1):  # 행의 번호: num
    info = list(map(int, sys.stdin.readline().strip()))
    for idx, value in enumerate(info):
        if value == 1:
            graph[idx+1].append(num)  # 거꾸로 집어넣는다.
            degree[num] += 1         # 갈 수 있는곳 degree check!

topology_sort(N)

if result.count(0) > 1:
    print(-1)
else:
    print(*result[1:])
