class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        length1 = len(nums1)
        length2 = len(nums2)
        if length1 > length2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        len_total = length1 + length2
        cut1, cut2 = 0, 0
        cutL, cutR = 0, length1
        while True:
            cut1 = (cutL + cutR) // 2
            cut2 = len_total // 2 - cut1
            L1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            L2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            R1 = float('inf') if cut1 == length1 else nums1[cut1]
            R2 = float('inf') if cut2 == length2 else nums2[cut2]
            
            if L1 > R2:
                cutR = cut1 - 1
            elif L2 > R1:
                cutL = cut1 + 1
            else:
                if len_total % 2 == 0:
                    L1 = L1 if L1 > L2 else L2
                    R1 = R1 if R1 < R2 else R2
                    return (L1 + R1) / 2
                else:
                    R1 = R1 if R1 < R2 else R2
                    return R1
                
        return -1
                
    #Solution on 1.21.2022
   class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        cut1, cut2 = 0, 0
        L1, R1 = 0, 0
        L2, R2 = 0, 0
        
        start, end = 0, m 
        while True:
            cut1 = (start + end) // 2
            cut2 = (m + n) // 2 - cut1
            L1 = nums1[cut1 - 1] if cut1 != 0 else float('-inf')
            R1 = nums1[cut1] if cut1 != m  else float('inf')
            L2 = nums2[cut2 - 1] if cut2 != 0 else float('-inf')
            R2 = nums2[cut2] if cut2 != n  else float('inf')
            if L1 > R2:
                end = cut1 - 1
            elif L2 > R1:
                start = cut1 + 1
            else:
                if (m + n) % 2 == 0:
                    L1 = max(L1, L2)
                    R1 = min(R1, R2)
                    return (L1 + R1) / 2
                else:
                    R1 = min(R1, R2)
                    return R1
        
            
        
        
        
