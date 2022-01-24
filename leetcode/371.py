'''
음수일 때를 고려하지 않은 풀이
'''
class Solution:
    def __init__(self) -> None:
        a = 2
        b = 3
        print(self.getSum(a,b))

    def getSum(self, a: int, b: int) -> int:
        c = 0
        while(b != 0):
            c = a&b
            a = a^b
            b = c<<1
        return a
Solution()
