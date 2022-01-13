class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            if nums[0] == target:
                return 0
            return -1
        
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if nums[mid] > target and nums[start] <= target:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target and nums[end] >= target:
                    start = mid
                else:
                    end = mid
            
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
        
