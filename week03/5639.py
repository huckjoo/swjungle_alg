import sys
sys.setrecursionlimit(10**9)
pre = []


def sol(start, end):
    if start > end:
        return
    root = pre[start]  # root는 항상 pre의 시작
    div = end + 1  # 종료조건
    for pos in range(start+1, end+1):  # 바뀌는 div를 찾는다.
        if pre[pos] > root:
            div = pos
            break
    sol(start+1, div-1)
    sol(div, end)
    print(root)


while True:
    try:
        pre.append(int(input()))
    except:
        break

sol(0, len(pre)-1)
