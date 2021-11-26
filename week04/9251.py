import sys

X = list(sys.stdin.readline().strip())
Y = list(sys.stdin.readline().strip())
n = len(X)
m = len(Y)
X.insert(0, 0)
Y.insert(0, 0)


lcs = [[0]*(m+1) for i in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        if X[i] == Y[j]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[n][m])
