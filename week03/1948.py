import sys
from collections import deque
n = int(sys.stdin.readline())  # 노드, 도시 개수
m = int(sys.stdin.readline())  # 도로의 개수
graph = [[]*(n+1) for _ in range(n+1)]
back_graph = [[]*(n+1) for _ in range(n+1)]  # 백트래킹용 그래프
indegree = [0]*(n+1)  # 진입차수
result = [0]*(n+1)
check = [0]*(n+1)
queue = deque()
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b, t))
    back_graph[b].append((a, t))
    indegree[b] += 1
start, end = map(int, sys.stdin.readline().split())

queue.append(start)  # indegree가 0인건 start점 밖에 없음


def topologysort():
    while queue:
        now = queue.popleft()
        for i, t in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+t)
            if indegree[i] == 0:
                queue.append(i)
    # 여기까지 하면 result에 최대 길이가 저장됨

    # 백트래킹 시작
    cnt = 0  # 임계경로에 속한 모든 정점의 개수
    queue.append(end)
    while queue:  # 도착점에서 시작점으로
        now = queue.popleft()
        for i, t in back_graph[now]:
            # 도착점까지의 비용에서 시작점의 비용을 뺐을 때 그 간선비용과 같다면
            if result[now]-result[i] == t:
                cnt += 1
                if check[i] == 0:  # 큐에 한번씩만 담을 수 있도록,중복방문제거
                    queue.append(i)
                    check[i] = 1

    print(result[end])
    print(cnt)


topologysort()
