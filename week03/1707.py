import sys

k = int(sys.stdin.readline())


def dfs(s):
    global cnt
    cnt += 1
    ch[s] = 1
    for i in graph[s]:
        if ch[i] == 0:
            dfs(i)


for i in range(k):
    cnt = 0
    v, e = map(int, sys.stdin.readline().split())
    ch = [0]*(v+1)
    graph = [[] for i in range(v+1)]
    for j in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    dfs(1)
    print(cnt)
    if cnt == v:
        print("YES")
    else:
        print("NO")
