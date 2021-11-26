N = 5

board = [[0]*N for i in range(N)]
for i in range(1, N):
    for j in range(0, N-i):
        print(j, j+i)
