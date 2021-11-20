import sys

sys.setrecursionlimit(10 ** 6)


def dfs(now, group):  # group을 1,-1로 나눔(빨강,파랑으로 색칠)
    vis[now] = group
    for i in arr[now]:
        # 아직 안가본 곳이면 방문
        if vis[i] == 0:
            if not dfs(i, -group):
                return False
        elif vis[i] == vis[now]:  # 방문한 곳인데, 방문한 곳의 group과 현재 group이 같다면
            return False
    return True  # 모든 dfs가 끝나고 true이면 true를 반환함


for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(v + 1)]
    vis = [0] * (v + 1)
    for _ in range(e):
        x, y = map(int, sys.stdin.readline().split())
        arr[x].append(y)
        arr[y].append(x)
    ans = True
    for i in range(1, v + 1):  # 이걸 왜 해줘야 하냐면 dfs로 한번에 다 돌지 못하는 그래프가 주어질 수도 있기 때문
        if vis[i] == 0:
            ans = dfs(i, 1)
            if not ans:
                break
    print("YES" if ans else "NO")
