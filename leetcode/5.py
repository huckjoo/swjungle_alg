# 혼자 푼 풀이
# Time Limit Exceeded
class Solution:
    def __init__(self) -> None:
        s = "babad"
        self.longestPalindrome(s)

    def longestPalindrome(self, s: str) -> str:
        s_list = list(s)
        N = len(s)
        maximum = -1
        ans = ""
        for i in range(N):
            for j in range(i+1, N):
                new = s_list[i:j+1]
                pl = 0
                pr = len(new)-1
                flag = 0
                while pl <= pr:
                    print("pl,pr", pl, pr)
                    if (new[pl] == new[pr]):
                        pl += 1
                        pr -= 1
                    else:
                        flag = 1
                        break
                if (flag == 0):
                    if len(new) > maximum:
                        ans = "".join(new)
                        maximum = len(new)
        print(ans)
        return ans


Solution()
