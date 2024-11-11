class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # subarray - 
        # max-len subarray
        # metric - diff between any two elements in the subarray
        # limitation of metric - less than limit
        # we will use left and right pointers
        left = 0
        minheap = []
        maxheap = []
        max_length = 0
        for right in range(len(nums)):
            heapq.heappush(minheap,(nums[right],right))
            heapq.heappush(maxheap,(-nums[right],right))
            # check current window valid
            while -maxheap[0][0]-minheap[0][0] > limit:
                # we remove ethier min element or max element depending on which comes before
                left = min(maxheap[0][1],minheap[0][1])+1
                while minheap[0][1] < left:
                    heapq.heappop(minheap)
                while maxheap[0][1] < left:
                    heapq.heappop(maxheap)
            max_length = max(max_length, right-left+1)
        return max_length
        

        
