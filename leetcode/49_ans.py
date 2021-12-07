# 상길북 참고
# defaultdict 이용
from typing import List
from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.groupAnagrams(strs)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            dict[key].append(word)
        return list(dict.values())


Solution()
