from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid[0])  # 열
        m = len(grid)    # 행
        queue = deque()
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        cnt = 0
        visited = [[False]*n for i in range(m)]
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1" and visited[y][x] == False:
                    cnt += 1
                    queue.append((y, x))
                    visited[y][x] = True
                    while queue:
                        cur_y, cur_x = queue.popleft()
                        for i in range(4):
                            nx = cur_x + dx[i]
                            ny = cur_y + dy[i]
                            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                                if visited[ny][nx] == False and grid[ny][nx] == "1":
                                    queue.append((ny, nx))
                                    visited[ny][nx] = True
        return cnt
