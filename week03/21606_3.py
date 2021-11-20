# 3점짜리 코드
import sys

n = int(sys.stdin.readline())
in_out = sys.stdin.readline().strip()

graph = [[] for i in range(n+1)]  # 0 ~ n까지
visited = [0]*(n+1)
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    except:
        break
cnt = 0


def dfs(now):
    global cnt
    if in_out[now-1] == '1':
        cnt += 1
    visited[now] = 1
    for x in graph[now]:
        if in_out[x-1] == '1' and visited[x] == 0:
            if in_out[now-1] == '1':
                cnt += 1
                return
            else:
                dfs(x)
    return


for i in range(1, n+1):
    dfs(i)

print(cnt)
