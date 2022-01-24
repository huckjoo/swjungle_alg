class Solution:
    def __init__(self) -> None:
        a = 2
        b = 3
        print(self.getSum(a,b))
    
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        while b != 0:
            a,b = (a^b) & MASK, ((a&b)<<1) & MASK
            print("a:",bin(a),"b:",bin(b))
        # 음수처리
        if a > INT_MAX:
            a = ~(a^MASK)
        
        return a

Solution()