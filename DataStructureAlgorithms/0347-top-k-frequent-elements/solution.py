class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxheap = []
        for num,freq in count.items():
            maxheap.append((-freq,num))
        heapq.heapify(maxheap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxheap)[1])
        return ans

        
