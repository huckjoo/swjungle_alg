# 혼자 푼 풀이 1560ms
class Solution:
    def __init__(self) -> None:
        s = "ccc"
        self.longestPalindrome(s)

    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        maximum = 1
        ans = s[0]
        for i in range(1, N):  # 홀수일때 check
            pl = i-1
            pr = i+1
            while (pr <= N-1 and pl >= 0):
                if s[pl] == s[pr]:
                    odd = s[pl:pr+1]
                    pl -= 1
                    pr += 1
                    if len(odd) > maximum:
                        maximum = len(odd)
                        ans = odd
                else:
                    break
        for i in range(N):  # 짝수일때 check
            pl = i
            pr = i+1
            while (pr <= N-1 and pl >= 0):
                if s[pl] == s[pr]:
                    even = s[pl:pr+1]
                    pl -= 1
                    pr += 1
                    if len(even) > maximum:
                        maximum = len(even)
                        ans = even
                else:
                    break
        return ans


Solution()
