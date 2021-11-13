import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        stack.append(int(data[1]))
    if data[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    if data[0] == 'size':
        print(len(stack))
    if data[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    if data[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
