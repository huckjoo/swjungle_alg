# 완전탐색으로 풀면 500000 * 500000 연산 수행 O(N^2) > 시간초과
import sys
from collections import deque
n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))

print(tops)
stack = deque()
s = n-1
e = n-1 - 1
if e < 0:  # n이 1일 때
    print(0)
else:  # n이 1이 아닐 때
    while True:  # s에 대한 while문
        if s == 0:  # s가 끝에 도달하면 종료
            stack.append(0)
            break
        flag = 0
        for e in range(s-1, -1, -1):  # e를 i로 돌린다. 이때 e의 시작은 s-1 e의 끝은 0
            if tops[s] < tops[e]:
                stack.append(e + 1)
                flag = 1
                break
        if flag == 0:
            stack.append(0)
        s -= 1
        e = s-1

stack.reverse()
for i in range(n):
    print(stack[i], end=' ')
