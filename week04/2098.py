import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


def TSP(board):
    N = len(board)
    all_visited = (1 << N)-1  # N개의 도시 체크됨
    # 행은 도시 개수(N)개에 대응, 열은 비트마스킹 하는 숫자들에 대응
    dp = [[None]*(1 << N) for i in range(N)]
    INF = float('inf')

    def path_find(last, visited):
        if all_visited == visited:  # 모든 도시를 방문했다면
            return board[last][0] or INF
        if dp[last][visited] is not None:  # 예전에 방문했던 곳이라면,
            return dp[last][visited]
        tmp = INF
        for city in range(N):
            # 길이 있고, 방문한 적 없는 도시라면,
            if board[last][city] != 0 and visited & (1 << city) == 0:
                tmp = min(tmp, path_find(city, visited |
                          (1 << city)) + board[last][city])
        dp[last][visited] = tmp  # 나중에 재사용하기 위해서 현재까지의 최대값을 저장해놓음
        return tmp

    return path_find(0, 1 << 0)  # 처음 visited 0번째만 visited되어 있어야함


print(TSP(board))
