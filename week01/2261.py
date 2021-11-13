import sys
n = int(sys.stdin.readline())
dots = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dots.sort()  # x좌표 기준으로 정렬


def find_dist(p, q):  # 바로 거리를 구한다.
    return (p[0]-q[0])**2 + (p[1]-q[1])**2


def dac(start, end):  # start는 첫 번째 점의 idx, end는 마지막 점의 idx
    # 종료조건
    if start == end:
        return 100000001
    if end - start == 1:  # 이분탐색하다가 점이 인접하게 된다면, 점이 2개만 남은것이다.
        return find_dist(dots[start], dots[end])
    # 분할정복 시작 >> 이분탐색시킴 (냅다 반으로 나누고 본다.)
    # 사실 분할정복은 나누기만 나누고 지금부터 진행시키는 코드(즉, 가운데부터)를 본다고 할 수 있겠다.
    mid = (start+end)//2
    min_dist = min(dac(start, mid), dac(mid+1, end))

    candidates = []  # 후보군들
    # x축 기준으로 min_dist와 (같거나)<-같은건 볼 필요가 없음 작은 후보군들을 고른다.
    for i in range(start, end+1):
        if (dots[mid][0]-dots[i][0])**2 < min_dist:
            candidates.append(dots[i])
    candidates.sort(key=lambda x: x[1])  # y축 기준으로 sort
    cdots = len(candidates)
    for i in range(cdots):
        for j in range(i+1, cdots):
            if (candidates[i][1]-candidates[j][1])**2 < min_dist:  # y축 기준 후보군
                temp = find_dist(candidates[i], candidates[j])
                min_dist = min(temp, min_dist)
            else:
                break
    return min_dist


print(dac(0, n-1))
