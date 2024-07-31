class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)
        ans=0
        while start<=end:
            print(f"start: {start}, end: {end}")
            mid=(start+end)//2
            print(f"mid: {mid}")
            hours=0
            for pile in piles:
                hours+=ceil(pile/mid)
            print(f"hours: {hours}")
            if hours>h:
                start=mid+1
            elif hours<=h:
                ans=mid
                end=mid-1
        return ans
                    
                

        
