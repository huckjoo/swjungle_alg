import sys


def get_area(heights):
    n = len(heights)
    if n == 1:
        return heights[0]
    mid = n//2
    l = mid - 1
    r = mid
    min_h = min(heights[l], heights[r])
    width = 2
    l_area = get_area(heights[:mid])
    r_area = get_area(heights[mid:])
    max_area = width * min_h
    while 0 <= l and r <= n-1:
        lh = heights[l-1] if l > 0 else 0
        rh = heights[r+1] if r < n-1 else 0
        if lh > rh:
            min_h = min(min_h, lh)
            l -= 1
        else:
            min_h = min(min_h, rh)
            r += 1
        width += 1
        max_area = max(max_area, min_h * width)
    return max(l_area, r_area, max_area)


while True:
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 0:
        break
    else:
        heights = data[1:]
    print(get_area(heights))
