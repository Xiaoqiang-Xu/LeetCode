class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n == 0:
            return -1
        left, right = 0, n - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] == target:
                right = mid
            else:
                right = mid
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
            
