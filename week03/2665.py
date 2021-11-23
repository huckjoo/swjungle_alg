import sys
from collections import deque

n = int(sys.stdin.readline())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(n)]

ch = [[0]*n for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dq = deque()

dq.append((0, 0))
ch[0][0] = 1
maze[0][0] = 0

while dq:
    y, x = dq.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if ch[ny][nx] == 0:  # 방문 안했으면
                if maze[ny][nx] == 0:  # 검은방이면
                    maze[ny][nx] = maze[y][x] + 1
                    ch[ny][nx] = 1
                    dq.append((ny, nx))
                else:  # 흰방이면
                    maze[ny][nx] = maze[y][x]
                    ch[ny][nx] = 1
                    dq.appendleft((ny, nx))
print(maze[n-1][n-1])
