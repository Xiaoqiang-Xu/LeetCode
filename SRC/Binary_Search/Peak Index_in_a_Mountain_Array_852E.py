class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] < arr[mid + 1]:
                start = mid
            else:
                end = mid
                
        if arr[start] > arr[end]:
            return start
        else:
            return end
        
