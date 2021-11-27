def tsp(D):
    N = len(D)
    inf = float('inf')
    ans = inf
    VISITED_ALL = (1 << N)-1

    def find_path(start, last, visited, tmp_dist):
        nonlocal ans  # nonlocal은 뭔가
        if visited == VISITED_ALL:  # 모든 도시를 방문했다면,
            return_home_dist = D[last][start] or inf
            # 지금까지 걸은 거리와 기존 도시로 돌아가는 거리를 더한 최종거리와 ans에 저장된 최종거리중 최소값
            ans = min(ans, tmp_dist + return_home_dist)
            return
        for city in range(N):
            # 방문한 적이 없고, 다음 city로 갈 수 있는 길이 있으면,
            if visited & (1 << city) == 0 and D[last][city] != 0:
                # visited에 city번호 원소 추가(1로 표시), 지금까지 거리에 다음거리 더해줌
                find_path(start, city, visited | (
                    1 << city), tmp_dist + D[last][city])

    for c in range(N):
        find_path(c, c, 1 << c, 0)  # 모든 도시에 대해서 수행

    return ans
