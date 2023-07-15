class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        cache[n] = cache[n-1] = 1
        for i in range(n-2,-1,-1):
            cache[i] = cache[i+1] + cache[i+2]
        return cache[0]
        
