# discuss 보고 푼 풀이
class Solution:
    def __init__(self) -> None:
        s = "babad"
        self.longestPalindrome(s)

    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)):
            ans = max(self.extendPalindrome(s, i, i),
                      self.extendPalindrome(s, i, i+1), ans, key=len)
        return ans

    def extendPalindrome(self, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        start = left+1
        end = right-1
        return s[start:end+1]


Solution()
