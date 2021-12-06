# 혼자서 품
# 단순 비교 -> 시간복잡도 O(N^2)예상 -> 5000ms
from typing import List


class Solution:
    def __init__(self) -> None:
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.groupAnagrams(strs)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ordered = []
        N = len(strs)
        checked = [False]*N
        for i in range(N):
            each_order = sorted(list(strs[i]))
            ordered.append(''.join(each_order))
        for i in range(N):
            box = []
            if checked[i] == False:
                box = [strs[i]]
                checked[i] = True
            for j in range(i+1, N):
                if checked[j] == False and ordered[i] == ordered[j]:
                    checked[j] = True
                    box.append(strs[j])
            if len(box) > 0:
                res.append(box)
        return res


Solution()
