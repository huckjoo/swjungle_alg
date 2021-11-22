# 200점 풀이
import sys
sys.setrecursionlimit(10**6)
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
ans = 0


def dfs(now, cnt):
    visited[now] = 1
    for x in graph[now]:  # now와 연결되어 있는 점들 중에서
        if visited[x] == 0:  # 방문하지 않은 경우,
            if in_out[x-1] == '1':  # 실내일 때
                cnt += 1
            else:  # 실외일때
                cnt = dfs(x, cnt)
    return cnt


def dfs1(now):
    global ans
    for x in graph[now]:  # now와 연결되어 있는 점들 중에서
        if in_out[x-1] == '1':  # 실내일 때
            ans += 1


for i in range(1, n+1):
    if in_out[i-1] == '0':  # 실외일때만 dfs를 실행시킴
        # 여기서 check해주지 않으면 매번 실행되서 오류가 남(한번 본 실외노드의 합은 다시 볼 필요가 없음)
        if visited[i] == 0:
            cnt = dfs(i, 0)
            ans += cnt*(cnt-1)
for i in range(1, n+1):
    if in_out[i-1] == '1':  # 실내일때만 dfs를 실행시킴
        dfs1(i)


print(ans)
