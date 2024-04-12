class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost0=[]
        lost1=[]
        counts=defaultdict(int)
        for match in matches:
            counts[match[0]]+=0
            counts[match[1]]+=1
        lost0=[k for k,v in counts.items() if v==0]
        lost1=[k for k,v in counts.items() if v==1]
        return [sorted(lost0),sorted(lost1) ]
        
