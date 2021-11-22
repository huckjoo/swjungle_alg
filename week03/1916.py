import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
INF = 1e8  # 1억
distance = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))  # a가 갈 수 있는 b와 cost (단방향 그래프)

start, end = map(int, sys.stdin.readline().split())


def get_minimum_dist():  # 방문된적 없고, 현재 값들중에서 최솟값을 찾아서 번호를 return
    min_dist = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_dist and not visited[i]:  # visited = False인 사람만 들어가서
            min_dist = distance[i]
            index = i
    return index


def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:  # 시작지점에서 갈 수 있는 녀석들부터 초기화
        if distance[i[0]] == INF:
            distance[i[0]] = i[1]
        else:
            distance[i[0]] = min(distance[i[0]], i[1])
    for _ in range(n-1):  # 시작지점 제외하고 반복
        now = get_minimum_dist()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]  # cost = now의 거리 + 도착지까지의 비용
            if cost < distance[j[0]]:  # cost가 도착지의 현재 거리보다 작다면
                distance[j[0]] = cost  # cost로 갱신


dijkstra(start)
print(distance[end])
