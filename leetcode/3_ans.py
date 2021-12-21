import sys
input = sys.stdin.readline


class Solution:
    def __init__(self) -> None:
        s = "abcabcbb"
        print(self.lengthOfLongestSubstring(s))

    def lengthOfLongestSubstring(self, s: str) -> int:
        len_max = 0
        for idx in range(len(s)):
            cnt = 0
            hash_table = [False]*128
            for ch in s[idx:]:
                i = ord(ch)
                if hash_table[i] == True:
                    break
                hash_table[i] = True
                cnt += 1
            if cnt > len_max:
                len_max = cnt
        return len_max


Solution()
