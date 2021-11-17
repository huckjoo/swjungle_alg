import sys
import heapq

n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)

L = int(sys.stdin.readline())
roads = []
for road in road_info:
    house, office = road
    if abs(house - office) <= L:  # 집과 사무실 사이의 거리가 철로 거리보다 작거나 같을 때만
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x: x[1])  # 길들 끝점 기준 오름차순으로 정렬

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - L:  # 끝점기준으로 철로에 포함되지 않는 road들은
            heapq.heappop(heap)  # pop해버림
            if not heap:  # heap에 아무것도 없다면
                break  # 멈춰!
        heapq.heappush(heap, road)  # 포함하는 놈들은 heap에 push해줌
    answer = max(answer, len(heap))

print(answer)
