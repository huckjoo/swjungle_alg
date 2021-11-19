import sys
sys.setrecursionlimit(10**9)


def f(start, end):  # 매개변수로 start, end가 들어감(pre에서의 마지막 idx)
    if start > end:  # start가 end보다 커지면 return
        return
    else:
        root = pre[start]  # root는 pre[0]이다(항상)
        div = end + 1     # div는 왜 end + 1인가?
        for pos in range(start+1, end+1):  # start + 1부터 end까지
            if root < pre[pos]:           # root보다 큰 놈이 나타나면 그때부터는 div를 pos로 바꿔준다.()
                div = pos
                break
        f(start+1, div-1)
        f(div, end)
        print(root)


pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break
if pre:
    f(0, len(pre)-1)
