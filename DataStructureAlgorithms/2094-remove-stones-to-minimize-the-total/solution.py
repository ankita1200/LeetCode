class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k>0:
            currpile = -heapq.heappop(piles)
            heapq.heappush(piles,(currpile//2) - currpile)
            k -= 1
        return -sum(piles)
        
        
