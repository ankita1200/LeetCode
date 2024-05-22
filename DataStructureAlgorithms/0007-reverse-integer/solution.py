class Solution:
    def reverse(self, x: int) -> int:
        a=2**31
        rev=0
        flag=False
        if x<0:
            flag=True
            x=x*(-1)
        while x>0:
            rev=rev*10 + x%10
            x=x//10
        if rev<a*-1 or rev>a-1:
            return 0
        return -1*rev if flag else rev
        
