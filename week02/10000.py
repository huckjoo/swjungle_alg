# import sys
# n = int(sys.stdin.readline())  # 원의 개수

n = 3
circle = [[2, 2], [1, 1], [3, 1]]
circles = []
# circles = []  # x좌표 최소, 최대 점으로 원들을 표시

# for i in range(n):
#     x, r = map(int, sys.stdin.readline().split())
#     a, b = x-r, x+r
#     circles.append([a, b])

for i in range(n):
    x, r = circle[i][0], circle[i][1]
    a, b = x-r, x+r
    circles.append([a, b])

cnt = 1
circles.sort(key=lambda x: (x[0], -x[1]))  # 오름차순 & 내림차순으로 정렬
print('circles:', circles)
stack = []  # 현재 최대 크기 원 저장공간
flag = 0
for i in range(n):
    while stack:
        # 원 안에 들어가지 않을 때는 그 전 값을 빼내서 항상 최대의 값을 유지하게 한다.
        if circles[i][0] > stack[-1][1]:
            stack.pop()
            flag = 0
        elif circles[i][0] == stack[-1][1]:  # 접하는 경우
            stack.append([circles[i][0], circles[i][1]])
            cnt += 1
            if stack[0][1] == circles[i][1] and flag == 1:  # 끝부분 접하는 경우
                cnt += 1
        else:  # 원 안으로 들어가는 경우
            if stack[-1][0] == circles[i][0]:  # 시작부분 같은경우
                flag = 1
            stack.append([circles[i][0], circles[i][1]])
            cnt += 1
    if len(stack) == 0:  # 스택이 비어있으면
        stack.append([circles[i][0], circles[i][1]])
        cnt += 1

print(cnt)
