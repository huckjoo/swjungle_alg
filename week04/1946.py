import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr.sort()
    cutline = arr[0][1]
    cnt = 1
    for i in range(1, N):
        if arr[i][1] < cutline:
            cutline = arr[i][1]
            cnt += 1
    print(cnt)
