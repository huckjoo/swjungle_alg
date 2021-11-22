import sys


def check(y, x):
    global M, N
    s = []
    cnt = 1
    visited = [[False]*M for _ in range(N)]
    visited[y][x] = True
    s.append((y, x))
    while s:
        y, x = s.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not visited[ny][nx] and board[ny][nx] != 0:
                s.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
melt = [[0]*M for i in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ice = []
for y in range(1, N-1):
    for x in range(1, M-1):
        if board[y][x] != 0:
            ice.append((y, x))

ans = 0
year = 0
while ice:
    # 여기서 len(ice)와 bfs로 센 개수가 다르면 바로 break, 맨 밑에 ans 출력
    if len(ice) != check(ice[0][0], ice[0][1]):
        ans = year
        break
    year += 1
    melted = []
    for i in range(len(ice)-1, -1, -1):  # 현재 빙산인 것들만 거꾸로 돌면서
        y, x = ice[i]
        for j in range(4):  # 빙산의 상하좌우를 확인하는데
            nx = x + dx[j]
            ny = y + dy[j]
            if board[ny][nx] == 0:  # 상하좌우중에 0이 있으면 cnt 개수를 올린다.
                melt[y][x] += 1
        if melt[y][x] > 0:  # 녹은 것이 있다면
            melted.append((y, x, i))  # melted에 저장
    for y, x, i in melted:
        board[y][x] -= melt[y][x]
        if board[y][x] <= 0:
            board[y][x] = 0
            ice.pop(i)
        melt[y][x] = 0
print(ans)
