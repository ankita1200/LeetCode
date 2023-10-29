class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def permutations(digits):
            if (len(str(digits)) == n):
                ans.add(digits)
                return
            if digits >= 10:
                last_digit = digits%10
            else:
                last_digit = digits
            if (last_digit-k) >= 0:
                permutations(digits*10 + last_digit-k)
            if (last_digit+k) < 10:
                permutations(digits*10+last_digit+k)
            return
        
        ans = set()
        for i in range(1,10):
            permutations(i)
        return ans
            
        
