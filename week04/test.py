import sys

N = int(sys.stdin.readline())
dists = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


def tsp(dists):
    N = len(dists)
    VISITED_ALL = (1 << N)-1
    dp = [[None]*(1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited):
        if visited == VISITED_ALL:  # 모든 도시를 방문했다면,
            # 다시 처음 도시로 갈 수 있으면 그 값을, 아니면 INF를 return하여 절대 답이 될 수 없게 함
            return dists[last][0] or INF
        if dp[last][visited] is not None:  # dp를 사용해서 한번 계산했으면 다시는 계산하지 않는다.
            return dp[last][visited]
        tmp = INF
        for city in range(N):
            # 방문한 적이 없고, 다음 city로 갈 수 있는 길이 있으면,
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp, find_path(city, visited |    # last를 city로 바꿔주고, visited 바꿔주고, 그 값에 가는 비용을 더한 값과 tmp를 비교한다.
                          (1 << city)) + dists[last][city])
        dp[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)


print(tsp(dists))
