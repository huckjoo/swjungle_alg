import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
needs = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    x, y, k = map(int, sys.stdin.readline().split())  # x를 만드는데 y부품 k개가 필요하다.
    graph[y].append((x, k))
    indegree[x] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for nxt, nxt_need in graph[now]:
        if needs[now].count(0) == n+1:  # 기본부품
            needs[nxt][now] += nxt_need
        else:  # 중간부품
            for i in range(1, n+1):
                if needs[now][i] != 0:
                    needs[nxt][i] += needs[now][i]*nxt_need
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

for idx, x in enumerate(needs[n]):
    if x > 0:
        print(idx, x)
