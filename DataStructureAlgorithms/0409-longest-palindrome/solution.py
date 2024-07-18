class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        ans=0
        maxval=0
        flag=True
        for ch,freq in count.items():
            if freq%2==0:
                ans+=freq
            elif flag:
                ans+=freq
                flag=False
            else:
                ans+=freq-1
        return ans
        
