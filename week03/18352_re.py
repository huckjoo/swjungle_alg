import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
ans = [-1]*(N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

ans[X] = 0
queue = deque()
queue.append(X)

while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        if ans[nxt] == -1:
            ans[nxt] = ans[now] + 1
            queue.append(nxt)
cnt = 0
res = []
for i in range(1, N+1):
    if ans[i] == K:
        cnt += 1
        res.append(i)
res.sort()
if cnt == 0:
    print(-1)
else:
    for x in res:
        print(x)
