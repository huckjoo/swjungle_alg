import sys
n, m = map(int, sys.stdin.readline().split())
# n: 나무의 수, m: 필요한 나무 길이
trees = list(map(int, sys.stdin.readline().split()))

res = []
pt = max(trees)
pb = 0
maxh = -1
while True:
    ph = (pt + pb)//2
    length = sum(tree-ph if tree > ph else 0 for tree in trees)
    if length == m:
        if maxh < ph:
            maxh = ph
        break
    elif length > m:
        pb = ph + 1
        if maxh < ph:
            maxh = ph
    elif length < m:
        pt = ph - 1
    if pb > pt:
        break

print(maxh)
