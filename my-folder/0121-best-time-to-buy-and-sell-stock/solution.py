class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = prices[0]
        largestdiff = 0
        for i in range(1,len(prices)):
            largestdiff= max(largestdiff, prices[i]-minsofar)
            minsofar= min(prices[i],minsofar)
        return largestdiff
        
        
