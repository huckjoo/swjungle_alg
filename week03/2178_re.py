import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= M-1 and 0 <= ny <= N-1:
                if maze[ny][nx] == 0:
                    continue
                if maze[ny][nx] == 1:
                    queue.append((ny, nx))
                    maze[ny][nx] = maze[y][x] + 1
    return maze[N-1][M-1]


print(bfs(0, 0))
