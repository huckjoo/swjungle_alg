import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
# n + 1 하는 이유 : 0번 인덱스부터 하면 헷갈리니까 맞추려고
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    from_n, to_n = map(int, sys.stdin.readline().split())
    matrix[from_n][to_n] = matrix[to_n][from_n] = 1  # 양방향

visit_list = [0] * (n + 1)  # 0번인덱스부터하면 헷갈리니까

for mat in matrix:
    print(mat)


def dfs(start_node):
    visit_list[start_node] = 1
    print(start_node, end=' ')
    for i in range(1, n + 1):  # 행을 돌면서 1부터 계속본다.(작은숫자부터 본다.)
        if visit_list[i] == 0 and matrix[start_node][i] == 1:   # 아직 방문안했는데 방문해야할 곳
            dfs(i)  # i를 다시 시작점에 넣고 재귀


def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visit_list[start_node] = 1

    while queue:
        start_node = queue.popleft()
        print(start_node, end=' ')
        for i in range(1, n + 1):
            if visit_list[i] == 0 and matrix[start_node][i] == 1:
                queue.append(i)
                visit_list[i] = 1


dfs(v)
print()
visit_list = [0] * (n + 1)
bfs(v)
