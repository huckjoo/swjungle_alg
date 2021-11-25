import sys
import heapq

n, K = map(int, sys.stdin.readline().split())  # n은 크기, k는 바이러스종류

board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

S, X, Y = map(int, sys.stdin.readline().split())  # S초 뒤에 X,Y에 있는 바이러스
visited = [[False]*(n) for i in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

time = 0
virus = []
heap = []

for x in range(n):
    for y in range(n):
        if board[x][y] != 0:
            num = board[x][y]
            heapq.heappush(heap, (num, x, y))
            visited[x][y] = True

for _ in range(S):
    next_virus = []
    while heap:
        now = heapq.heappop(heap)
        k, x, y = now[0], now[1], now[2]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = k
                    next_virus.append((k, nx, ny))
    for vir in next_virus:
        heapq.heappush(heap, vir)

print(board[X-1][Y-1])
