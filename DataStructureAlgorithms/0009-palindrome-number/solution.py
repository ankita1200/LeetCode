class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        l = len(st)
        if l==0:
            return True
        for i in range(ceil(l/2)):
            if st[i] != st[l-1-i]:
                return False
        return True

        
