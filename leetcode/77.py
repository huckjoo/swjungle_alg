from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(elements, start, k):
            # 종료조건
            if k == 0:
                ans.append(elements[:])
                return
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        dfs([], 1, k)
        return ans
