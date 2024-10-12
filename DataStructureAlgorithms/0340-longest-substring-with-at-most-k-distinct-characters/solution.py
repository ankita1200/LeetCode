class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        hmap = {}
        ans = 0
        n = len(s)
        left = 0
        count = 0
        for right in range(n):
            if s[right] in hmap:
                hmap[s[right]] += 1
            else:
                hmap[s[right]] = 1
                count += 1
                if count > k:
                    while count > k:
                        hmap[s[left]] -= 1
                        if hmap[s[left]] == 0:
                            del hmap[s[left]]
                            left += 1
                            count -= 1
                            break
                        left += 1
            ans = max(ans,right-left+1)
        return ans

                
        
