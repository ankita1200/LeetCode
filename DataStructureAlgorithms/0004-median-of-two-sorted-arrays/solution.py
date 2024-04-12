class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        if m == 0 and n == 0:
            return 
        if m == 0:
            return nums2[int(n/2)] if n % 2 !=0 else (nums2[int(n/2)]+nums2[int(n/2-1)])/2
        if n == 0:
            return nums1[int(m/2)] if m % 2 !=0 else (nums1[int(m/2)]+nums1[int(m/2-1)])/2
        fin = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                fin.append(nums1[i])
                i +=1
            else:
                fin.append(nums2[j])
                j +=1
        while i < m:
            fin.append(nums1[i])
            i += 1
        while j < n:
            fin.append(nums2[j])
            j += 1
        
        if (m+n)%2 == 0:
            mid1 = (m+n)/2
            mid2 = mid1-1
            return (fin[int(mid1)]+fin[int(mid2)])/2
        else:
            return fin[int((m+n-1)/2)]
                
                
        
