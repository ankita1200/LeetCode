class Solution:
    def isHappy(self, n: int) -> bool:
        it = 0
        while n != 1:
            newnum = 0
            while n > 0:
                newnum = newnum + int(n %10)**2
                n = n // 10
            n = newnum
            if n==4:
                return False
        return True
        
