M, N, L = map(int, input().split())  # M 사대의 수, N 동물의 수, L 사정거리
pos = list(map(int, input().split()))  # pos 사대의 위치 animal_pos 동물의 위치
temp = []
animal_pos = ani = [list(map(int, input().split())) for i in range(N)]
pos.sort()
# y값이 L을 이미 벗어난 경우 제외
for a in temp:
    if a[1] <= L:
        animal_pos.append(a)
total_kill = 0
for x, y in animal_pos:
    pl = 0
    pr = len(pos)-1
    while pl <= pr:  # 사대는 x축으로 정렬되어있고 여기서 가장 가까운 x 좌표를 찾는다.
        pc = (pl + pr)//2
        if abs(pos[pc] - x) <= L - y:
            total_kill += 1  # 발견하면 동물은 잡을 수 있는 것이고 break를 해 준다.
            break
        else:
            if pos[pc] > x:
                pr = pc - 1
            else:
                pl = pc + 1
print(total_kill)
