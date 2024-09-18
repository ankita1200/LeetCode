class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n<1:
            return 0
        for paper in range(n,0,-1):
            count = 0
            for i in range(n):
                if citations[i] >= paper:
                    count += 1
            if paper<=count:
                return paper
        return 0
        

        
