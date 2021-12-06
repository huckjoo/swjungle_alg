# discuss 참고
# dictionary를 이용 -> 100ms (시간복잡도 1/50 로 줄어듬)
from typing import List


class Solution:
    def __init__(self) -> None:
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.groupAnagrams(strs)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            key = tuple(sorted(word))
            dict[key] = dict.get(key, []) + [word]
        return list(dict.values())


Solution()
