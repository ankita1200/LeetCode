class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for i in range(len(t)):
            d[t[i]] += 1
        left = 0
        minwindow = float('inf')
        start = 0
        end = 0
        #keeps track of the restriction on constraint metric
        count = 0
        #counts the frequency of elements of t in the current window
        # this is the constraint metric
        freq = defaultdict(int)
        for right in range(len(s)):
            if s[right] in d:
                freq[s[right]] +=1
                if freq[s[right]]<= d[s[right]]:
                    count += 1
            # we move the left pointer until we find the next invalid window
            while count==len(t):
                #we are having a valid window
                currwindow = right - left + 1
                if currwindow < minwindow:
                    start = left
                    end = right+1
                    minwindow = currwindow
                
                if s[left] in d:
                    freq[s[left]] -=1
                    if freq[s[left]] < d[s[left]]:
                        count -= 1
                left +=1
        return s[start:end]

            
