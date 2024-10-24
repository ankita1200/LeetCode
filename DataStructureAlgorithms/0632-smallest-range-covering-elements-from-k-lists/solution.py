class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        merged = []
        for i in range(len(nums)):
            for num in nums[i]:
                merged.append((num,i))
        
        merged.sort()
        left = 0
        start_range, end_range = 0, float('inf')
        # this counter keeps track of number of lists from which we have an element in the current range.This counter is used to check if the current window is valid range.
        count = 0
        # This keeps track of frequency of elements from each list in the current window.
        freq = defaultdict(int)
        for right in range(len(merged)):
            freq[merged[right][1]] += 1
            if freq[merged[right][1]]==1:
                # implies this element if one of the first from the its parent list to be included in the current window
                count += 1
            
            #check if the current window is a valid window
            while count==len(nums):
                #we have a new valid window that can be possible answer
                curr_range = merged[right][0] - merged[left][0]
                if curr_range < end_range - start_range:
                    #update the ans
                    start_range = merged[left][0]
                    end_range = merged[right][0]
                
                freq[merged[left][1]] -= 1
                if freq[merged[left][1]]==0:
                    count -= 1
                #increment the left pointer, to explore a new window
                left += 1
                
        return [start_range, end_range]

        
