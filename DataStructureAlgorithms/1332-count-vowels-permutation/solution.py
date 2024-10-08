class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        constraint = {'a':['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
        
        @cache
        def dp(index,prev_vowel):
            if index==n:
                return 1
            c = ['a','e','i','o','u']
            if prev_vowel in constraint:
                c = constraint[prev_vowel]
            count = 0
            for vow in c:
                count += dp(index+1,vow)
            return count
        
        return dp(0,'') % (10**9 + 7)
