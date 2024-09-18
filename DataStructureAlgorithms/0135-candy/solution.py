class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        for i in range(n-1):
            if ratings[i] > ratings[i+1] and candies[i]<=candies[i+1]:
                candies[i] = candies[i+1]+1
            elif ratings[i] < ratings[i+1] and candies[i+1]<=candies[i]:
                candies[i+1] =candies[i]+1
        

        for j in range(n-1,0,-1):
            if ratings[j] > ratings[j-1] and candies[j]<=candies[j-1]:
                candies[j] = candies[j-1]+1
            elif ratings[j] < ratings[j-1] and candies[j-1]<=candies[j]:
                candies[j-1] =candies[j]+1            
        return sum(candies) 
        
