class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        st=5
        pow=1
        while st <= n:
            count += n // st
            pow = pow + 1
            st = 5**pow
        return count
        
