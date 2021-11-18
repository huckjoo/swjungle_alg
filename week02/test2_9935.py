import sys

data = sys.stdin.readline().strip()
data = list(data)
bomb = sys.stdin.readline().strip()
stack = []
l = len(bomb)
while len(data) > 0:
    flag = 0
    n = data.pop()
    stack.append(n)
    if n == bomb[0] and len(stack) >= l:
        flag = 1
        for i in range(l):
            if bomb[i] != stack[-1-i]:
                flag = 2
        if flag == 1:
            for i in range(l):
                stack.pop()
stack.reverse()
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
