def check(y, x):  # 두 개로 나눠진지 아닌지 check하는 함수
    global N, M
    cnt = 1
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    s = [(y, x)]

    while s:         # 이 방법은 bfs 인것같다.
        y, x = s.pop()

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not visited[ny][nx] and arr[ny][nx] != 0:  # 만약 방문하지 않았고, 빙산이라면
                s.append((ny, nx))                        # s에 좌표를 넣어준다.
                visited[ny][nx] = True                    # 좌표 방문처리 한다.
                cnt += 1                                  # cnt를 1 올린다.

    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
melt = [[0] * M for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

ice = []
for i in range(1, N-1):  # 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워지니까 그 안쪽만 scan
    for j in range(1, M-1):
        if arr[i][j] != 0:
            ice.append((i, j))

ans = 0
year = 0
while ice:
    # 현재 빙산의 개수와 이어진 빙산의 개수를 탐색했을 때 다르다면 두개로 나눠진거고,
    if len(ice) != check(ice[0][0], ice[0][1]):
        ans = year  # 그럼 답을 출력한다.
        break
    year += 1
    melt_co = []
    for i in range(len(ice) - 1, -1, -1):  # ice에 있는 모든 원소들을 뒤에서부터 돌면서
        y, x = ice[i]

        for dir in range(4):  # 여기서는 조건을 check할필요가 없는게 모든 바깥이 바다로 둘러쌓여있기 때문
            ny = y + dy[dir]
            nx = x + dx[dir]

            if arr[ny][nx] == 0:   # 바다 옆에 붙어있으면
                melt[y][x] += 1    # 녹는다.

        if melt[y][x] > 0:         # 녹았으면
            # melt_co에 녹은 y,x좌표와 ice의 좌표인 i를 저장한다.(얘는 나중에 ice에서 빼주려고 설정)
            melt_co.append((y, x, i))
    print('melt_co:', melt_co)
    for y, x, i in melt_co:
        arr[y][x] -= melt[y][x]
        if arr[y][x] <= 0:
            arr[y][x] = 0
            print('ice:', ice)
            print(i, ice[i])
            # melt_co를 뒤에서부터 넣어놨기 때문에 i가 뒤에꺼부터 빠지고, ice에서 i는 앞에서부터이기 때문에 다른 i들이 pop(i)의 영향x
            ice.pop(i)

        melt[y][x] = 0  # melt 초기화

print(ans)
