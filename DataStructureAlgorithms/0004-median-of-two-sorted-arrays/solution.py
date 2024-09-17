class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n2 < n1:
             nums1, nums2, n1, n2 = nums2, nums1, n2, n1
        low = 0
        high = len(nums1)
        while low <= high:
            cut1 = (low + high) // 2
          
            cut2 = (n1+n2)//2 - cut1
            
            l1 = float('-inf') if cut1==0 else nums1[cut1-1]
            l2 = float('-inf') if cut2==0 else nums2[cut2-1]
            r1 = float('inf') if cut1==n1 else nums1[cut1]
            r2 = float('inf') if cut2==n2 else nums2[cut2]
            if l1 > r2:
                high = cut1 - 1
            elif l2 > r1:
                low = cut1 + 1
            else:
                if (n1+n2) % 2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return min(r1,r2)
        


        
