import sys

# N : 최종 돌의 숫자, M : 착지할 수 없는 작은 돌의 갯수
N, M = map(int, sys.stdin.readline().split())

# DP 테이블(행은 단계별 돌의 숫자, 열은 속도)
# DP[i][j]의 의미는 i번째 돌에 j의 속도로 도착할 때의 점프 횟수
# 초깃 값은 'inf'로 설정한다.
# 최대 속도는 1부터 N까지 속도를 1씩 늘려간다고 했을 때의 근사 값이다.
DP = [[float('inf')] * (int((2 * N) ** 0.5) + 2) for _ in range(N + 1)]
DP[1][0] = 0

# 착지할 수 없는 돌들을 set에 넣어준다.
passing = set(int(sys.stdin.readline().rstrip()) for _ in range(M))

# 돌을 단계별로 하나씩 늘려간다.
for num_stone in range(2, N + 1):
    # 도착하려고 하는 돌이 passing에 있으면 넘어간다.
    if num_stone in passing:
        continue

    # 해당 돌에 도착할 수 있는 속도를 케이스별로 살펴본다.
    for velocity in range(1, int((2 * num_stone) ** 0.5) + 1):
        # DP[돌][속도]는 해당 돌에 도착하기 전 단계를 고려해야한다.
        # 즉, 이전 단계의 속도보다 1 감속한 경우이거나, 이전 단계와 속도가 같은 경우이거나, 이전 단계보다 속도를 1 가속한 경우이다.
        DP[num_stone][velocity] = min(DP[num_stone-velocity][velocity-1],
                                      DP[num_stone-velocity][velocity], DP[num_stone-velocity][velocity+1]) + 1

if min(DP[N]) == float('inf'):
    print(-1)
else:
    print(min(DP[N]))
