import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())  # V는 정점의 개수, E는 간선의 개수
visited = [False]*(V+1)          # 방문여부 확인, 정점은 1번부터 매겨져 있으므로 V+1개
Elist = [[] for _ in range(V+1)]  # 간선 저장

heap = [[0, 1]]                  # 현재 그래프에서 짧은 경로 선택
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])

answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

print(answer)
