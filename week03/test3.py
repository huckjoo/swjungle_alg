import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 양방향 그래프

start, end = map(int, sys.stdin.readline().split())


def bfs(start, end, maximum):
    queue = deque()
    queue.append(start)
    visited = set()    # visited[i]=True 보다 set이 더 빠르다.
    visited.add(start)  # queue에서 뺄때마다 visited에 넣어주지 말고
    while queue:       # queue에 넣어주면서 visited check해주는게 더 빠르다.
        now = queue.popleft()
        for nxt, limit in graph[now]:
            if nxt not in visited and limit >= maximum:
                queue.append(nxt)
                visited.add(nxt)
    if end in visited:  # 방문했으면
        return True
    else:
        return False


pl = 1
pr = 1000000000

ans = pl
while pl <= pr:
    mid = (pl+pr)//2
    if bfs(start, end, mid):
        ans = mid
        pl = mid + 1
    else:  # 중량 줄여봐야함
        pr = mid-1
print(ans)
