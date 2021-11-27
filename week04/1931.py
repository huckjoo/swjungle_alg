import sys

N = int(sys.stdin.readline())
meetings = []
for i in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# 뒤에꺼 정렬해주고 앞에껄 정렬해줘야 우리가 원하는 순서로 정렬이 완성됨
meetings.sort(key=lambda x: x[1])
meetings.sort(key=lambda x: x[0])

stack = []

while meetings:
    start, end = meetings.pop()
    if len(stack) == 0:
        stack.append(start)
    else:
        if stack[-1] >= end:
            stack.append(start)

print(len(stack))
