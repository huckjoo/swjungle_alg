from collections import defaultdict


class Solution(object):
    def __init__(self) -> None:
        numCourses = 5
        prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
        print(self.canFinish(numCourses, prerequisites))

    def canFinish(self, numCourses, prerequisites):
        traced = set()
        visited = set()
        graph = defaultdict(list)
        for pre in prerequisites:
            x, y = pre
            graph[x].append(y)

        def dfs(i):
            # 방문했던곳 또 방문할경우
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for nxt in graph[i]:
                if not dfs(nxt):
                    return False
            traced.remove(i)  # for문 안쪽에 넣으면 안됨! 정확한 이유는?
            visited.add(i)  # 모든 순회가 끝나면 visited에 추가.
            return True

        # 순환구조 판별, 하나라도 있으면 False
        for x in list(graph):
            if not dfs(x):
                return False
        # 없으면 True
        return True


Solution()
