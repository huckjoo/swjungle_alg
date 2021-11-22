# 먼저 입력으로 들어오는 구슬 번호대로 무게 순서를 지켜 관계를 2차원 리스트에 1로 표시해 줍니다.
# 다음으로 플로이드-와샬 알고리즘을 통해 모든 구슬들의 연결 관계를 확인해서 표시해 줍니다.
# 최종적으로 연결관계가 표시된 이차원 리스트에서 2중 반복문을 돌면서 무게가 크거나 작은 구슬들의 개수를 세어줍니다.
# 크거나 작은 구슬들의 개수가 N/2 보다 크다면 중간값이 될 수 없으므로 개수를 세어줍니다

import sys
input = sys.stdin.readline
# 모든 구슬들의 관계를 살펴보고 조건 확인하기

N, M = map(int, input().split())

arr = [[0]*(N+1) for _ in range(N+1)]


for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1  # 방향 그래프 s -> e 이것의 의미는 s > e이다.

# 플로이드 워셜                           # 모든 노드들의 대소비교를 할 수 있다.
for k in range(1, N+1):                  # k는 거쳐가는 노드
    for i in range(1, N+1):              # i는 출발 노드
        for j in range(1, N+1):          # j는 도착 노드
            if arr[i][k] and arr[k][j]:  # i > k 이고 k > j 이면
                arr[i][j] = 1            # i > j이다.

ans = 0

for i in range(1, N+1):
    left_cnt = 0
    right_cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        elif arr[i][j] == 1:  # 현재 구슬보다 가벼운 갯수 세기
            right_cnt += 1
        elif arr[j][i] == 1:  # 현재 구슬 보다 무거운 갯수 세기
            left_cnt += 1
    if right_cnt > N//2 or left_cnt > N//2:  # 가볍거나 무거운 개수가 중간값 보다 많으면 될 수가 없다
        ans += 1


print(ans)
