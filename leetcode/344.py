# 344. reverse-string
# 투포인터 사용
def reverseString(s):
    N = len(s)
    pl = 0
    pr = N-1
    while pl < pr:
        s[pl], s[pr] = s[pr], s[pl]
        pl += 1
        pr -= 1
    return s


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))
