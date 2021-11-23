# 위상정렬이란 이런거다.
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    now = queue.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
for x in result:
    print(x, end=' ')
