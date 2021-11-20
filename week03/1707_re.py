import sys
sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline())


def dfs(now, group):
    visited[now] = group
    for x in graph[now]:
        if visited[x] == 0:  # 방문한적이 없으면
            if not dfs(x, -group):   # -group 하고 다음거 방문
                return False
        elif visited[x] == visited[now]:
            return False     # 여기서 False를 return하게 되면 그 dfs만 return이 False가 된다. 따라서 전체함수를 False로
            # 만들어주기 위해서는 조건을 추가해줘야 한다.
    return True


for i in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v+1)]
    visited = [0]*(v+1)
    for j in range(e):  # 그래프 완성
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = True
    for c in range(1, v):
        if visited[c] == 0:
            ans = dfs(c, 1)
            if ans == False:
                break
    if ans == True:
        print("YES")
    else:
        print("NO")
