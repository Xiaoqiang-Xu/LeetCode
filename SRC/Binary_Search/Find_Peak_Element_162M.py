class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return -1
        
        start, end = 0, n - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        
        return start
        
