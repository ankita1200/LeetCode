class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        ans = {}
        for num in sorted(nums):
            maxsubset = set()
            for k,v in subsets.items():
                if num%k==0 and len(v) > len(maxsubset):
                    maxsubset = v
            subsets[num] = maxsubset | {num}
            if len(subsets[num]) > len(ans):
                ans = subsets[num]
        return list(ans)
