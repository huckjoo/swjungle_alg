import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A.sort()  # 이분탐색은 정렬후에 사용가능
for x in B:
    pl = 0
    pr = len(A)-1
    while True:
        pc = (pr+pl)//2
        if A[pc] == x:  # 찾았을 때
            print(1)
            break
        elif x > A[pc]:
            pl = pc+1
        elif x < A[pc]:
            pr = pc-1
        if pl > pr:  # 못 찾았을때
            print(0)
            break

# 선형탐색은 시간초과됨
