# 스택으로 풀어보자!
import sys
n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))

stack = []  # 현재 최대값 (레이저 신호를 수신하는 탑)
ans = []  # 답을 입력하는 곳

for i in range(n):
    while stack:  # 수신가능한 탑이 있는 상황이면,
        if stack[-1][1] < tops[i]:  # 현재 값이 지금까지 최대값보다 크다면
            stack.pop()
        else:
            ans.append(stack[-1][0]+1)
            stack.append([i, tops[i]])
            break
    if len(stack) == 0:
        ans.append(0)
        stack.append([i, tops[i]])
for i in range(n):
    print(ans[i], end=" ")
