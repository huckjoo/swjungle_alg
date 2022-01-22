'''
너무 한가지 풀이방식을 고집하지 말자
'''
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y = 0
        x = len(matrix[0])-1
        
        while x>=0 and y <= len(matrix)-1:
            if target == matrix[y][x]:
                return True
            elif target > matrix[y][x]:
                y += 1
            elif target < matrix[y][x]:
                x -= 1
        return False