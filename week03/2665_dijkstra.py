import sys
import heapq

n = int(sys.stdin.readline())
maze = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(n)]

ch = [[0]*n for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

heap = []

heapq.heappush(heap, (0, 0, 0))  # 가중치(지금까지의 거리), y좌표, x좌표
ch[0][0] = 1

while heap:
    dist, y, x = heapq.heappop(heap)
    if y == n-1 and x == n-1:
        print(dist)
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if ch[ny][nx] == 0:  # 방문 안했으면
                if maze[ny][nx] == 0:  # 검은방이면
                    heapq.heappush(heap, (dist+1, ny, nx))
                else:  # 흰방이면
                    heapq.heappush(heap, (dist, ny, nx))
                ch[ny][nx] = 1
# print(maze[n-1][n-1])
# 다익스트라는 maze 자체를 바꾸지 않고 안에서 돌기 때문에
# print(maze[n-1][n-1]) 이렇게 직접 접근하지 말고 돌다가 찾아야함
