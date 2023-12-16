class Solution:
    def countElements(self, arr: List[int]) -> int:
        dct = {}
        for x in arr:
            dct[x] = dct.get(x,0) + 1
        ans = 0
        for key, val in dct.items():
            if key+1 in dct:
                ans += val
        return ans
            
        
