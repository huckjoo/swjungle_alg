import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
back_graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
res = [0]*(n+1)
ch = [0]*(n+1)

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b, t))
    back_graph[b].append((a, t))
    indegree[b] += 1

start, end = map(int, sys.stdin.readline().split())
queue = deque()
cnt = 0


def topology_sort():
    global cnt
    queue.append(start)
    while queue:
        now = queue.popleft()
        for i, t in graph[now]:
            res[i] = max(res[i], res[now]+t)
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    # 백트래킹
    queue.append(end)
    while queue:
        now = queue.popleft()
        for i, t in back_graph[now]:
            if res[now]-res[i] == t:  # 최대일때만 찾아감
                cnt += 1  # 얘 위치가 여기가 맞나?
                if ch[i] == 0:
                    queue.append(i)
                    ch[i] = 1


topology_sort()
print(res[n])
print(cnt)
