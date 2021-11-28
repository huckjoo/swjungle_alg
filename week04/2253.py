import sys
n, m = map(int, sys.stdin.readline().split())

max_speed = int((2*n)**0.5) + 1  # dp테이블 메모리 최소화시키기
dp_table = [[10001] * (max_speed+1) for i in range(n+1)]
# dp_table[i][j] / [i] = 돌 번호  [j] = acc

small_stone = set()

for _ in range(m):
    small_stone.add(int(sys.stdin.readline()))


dp_table[2][1] = 1

for step in range(3, n+1):
    if step in small_stone:
        continue
    for speed in range(1, max_speed):
        dp_table[step][speed] = min(dp_table[step - speed][speed - 1],
                                    dp_table[step - speed][speed],
                                    dp_table[step - speed][speed + 1]) + 1

answer = min(dp_table[n])

if answer == float('inf'):
    print(-1)
else:
    print(answer)
