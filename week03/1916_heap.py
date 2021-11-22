# 개수가 적어서 그런지 heap이 더 오래걸렸다... 정확히 이해하지 못한듯(한번 다시 봐야함)
import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
INF = 1e8  # 1억
distance = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))  # a가 갈 수 있는 b와 cost (단방향 그래프)

start, end = map(int, sys.stdin.readline().split())


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)  # 최소거리가 출력됨
        if dist > distance[now]:
            continue
        for nxt in graph[now]:
            # dist는 now의 cost, nxt[1]은 다음 녀석의 cost
            cost = dist + nxt[1]
            if distance[nxt[0]] > cost:   # nxt[0]은 다음 녀석의 b(목적지)
                distance[nxt[0]] = cost
                heapq.heappush(heap, (cost, nxt[0]))


dijkstra(start)
print(distance[end])
