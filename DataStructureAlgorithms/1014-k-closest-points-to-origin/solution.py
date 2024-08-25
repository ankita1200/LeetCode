class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = (x*x + y*y)**(1/2)
            heapq.heappush(heap,(-dist,x,y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x,y] for dist,x,y in heap]
        
        
        
            
        
