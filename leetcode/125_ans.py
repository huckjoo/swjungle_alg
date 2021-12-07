# 125. Valid Palindrome
# 투포인터
def isSame(a, b):

    if a.lower() == b.lower():
        return True
    else:
        return False


def isPalindrome(s):
    pl = 0
    pr = len(s)-1
    while pl <= pr:
        if s[pl].isalnum() and s[pr].isalnum():
            left = s[pl]
            right = s[pr]
            if isSame(left, right):
                pl += 1
                pr -= 1
            else:
                return False
        if not s[pl].isalnum():
            pl += 1
        if not s[pr].isalnum():
            pr -= 1
    return True


s = "0P"
print(isPalindrome(s))
