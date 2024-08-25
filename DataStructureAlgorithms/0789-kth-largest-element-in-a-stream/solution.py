class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        popno = len(nums)-k
        while popno>0:
            heapq.heappop(self.heap)
            popno -= 1
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap) == self.k:
            return self.heap[0]
        heapq.heappop(self.heap)
        return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
