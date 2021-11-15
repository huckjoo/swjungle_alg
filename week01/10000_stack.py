import sys

n = int(sys.stdin.readline())
circles = []
for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    a, b = x-r, x+r
    circles.append([0, a])
    circles.append([1, b])

points = sorted(circles, key=lambda x: (x[1], -x[0]))


# 차례대로 돌며 확인
stack = []
cnt = 1
for curr in points:
    # 왼쪽끝인 경우
    if curr[0] == 0:
        stack.append(curr)
        continue
    # 오른쪽끝인 경우
    acc_width = 0
    while stack:
        prev = stack.pop()
        # 본인 내부에 원이 있었으면, 해당 원의 너비를 누적
        if prev[0] == "c":
            acc_width += prev[1]
        # R이 나올 때마다 L를 pop해주므로 처음 만난 L이 본인과 동일한 원에서 나온 값
        elif prev[0] == 0:
            # 원의 너비 계산
            width = curr[1] - prev[1]
            # 내부에 있는 원들의 너비 합산이 본인의 너비와 일치하는지 확인
            if width == acc_width:
                cnt += 2
            else:
                cnt += 1
            # 다른 원에 포함될 수 있으므로 추가
            stack.append(("c", width))
            break

print(cnt)
