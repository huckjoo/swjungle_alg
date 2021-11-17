import sys


def getRect(heights): # heights라는 리스트를 넣어서 가장 큰 직사각형을 반환하는 함수
    n = len(heights)  # hegihts의 개수
    if n == 1:        # n이 1이면, 
        return heights[0] # 그 리스트의 하나남은 값을 반환한다.
    mid = n // 2          # mid는 분할정복을 위해 개수의 반이다. 5//2 > 2, 6//3 > 2
    left_h = getRect(heights[:mid]) # left_h는 getRect()에 heights의 처음부터 mid-1까지의 리스트를 넣는다.
    right_h = getRect(heights[mid:]) # right_h는 getRect()에 heights의 mid부터 끝까지의 리스트를 넣는다.
    l = mid - 1                     # l은 mid-1(경계선 왼쪽 직사각형)
    r = mid                         # r은 mid(경계선 오른쪽 직사각형)
    under_w = 2                     # under_w는 width, 현재는 2
    min_h = min(heights[l], heights[r]) # l과 r의 heights를 비교해서 최솟값을 min_h로 정함
    max_area = under_w * min_h          # min_h와 under_w를 곱해서 현재 최대넓이를 저장함

    while 0 <= l and r + 1 <= n:             # l은 0 이상이고, r은 n-1이하면 while문이 돌아감 
        # 위의 while문에서 굳이굳이 이상이하를 붙여준 이유는 끝났을 때 0을 집어넣는 조건을 추가하기 위해서이다.
        lh = heights[l-1] if l >= 1 else 0   # l>=1이면 heights[l-1]을 lh에 집어넣고 아니라면 0을 집어넣는다.
        rh = heights[r+1] if r < n-1 else 0  # r < n-1이면 heights[r+1]을 rh에 집어넣고 아니라면 0을 집어넣는다.
        min_h = min(min_h, lh) if lh > rh else min(min_h, rh) # lh와 rh를 비교해서 lh가 크다면 min_h와 lh를, rh가 크다면 min_h와 rh를 비교해서 작은걸 min_h에 저장
        if lh > rh: # lh가 크다면 l-=1을 해서 그쪽 사각형 먼저 채우고 어차피 끝까지 가서 0이 들어간다. 0이 들어간 후에는 무조건 반대편이 움직인다.
            l -= 1
        else:       # rh가 크다면 r+=1을 해서 그쪽 사각형 먼저 채우고 어차피 끝까지 가서 0이 들어간다. 0이 들어간 후에는 무조건 반대편이 움직인다.
            r += 1 
        under_w += 1 # 한번 움직일 때마다 width가 증가한다.
        max_area = max(max_area, under_w * min_h) # 최대넓이는 현재 최대넓이와 지금 늘어난 width와 min_h의 곱을 비교해서 큰 값을 유지시킨다.

    return max(left_h, right_h, max_area) # 왼쪽, 오른쪽, 가운데 최대값을 다 확인한다.


while True:
    heights = list(map(int, sys.stdin.readline().split()))
    if len(heights) == 1 and heights[0] == 0:
        break
    print(getRect(heights[1:]))
