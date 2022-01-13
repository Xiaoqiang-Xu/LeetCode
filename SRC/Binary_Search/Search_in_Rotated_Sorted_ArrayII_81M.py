class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        if n == 0:
            return False
        if n == 1:
            if nums[0] == target:
                return True
            return False
        
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid]:
                start += 1
                continue
            targetInFirst = self.existsInFirst(nums, start, target)
            if nums[mid] > nums[start] and not targetInFirst:
                start = mid
            elif nums[mid] < nums[start] and targetInFirst:
                end = mid
            elif nums[mid] > nums[start] and targetInFirst:
                if nums[mid] < target:
                    start = mid
                else:
                    end = mid
            elif nums[mid] < nums[start] and not targetInFirst:
                if nums[mid] < target:
                    start = mid
                else:
                    end = mid
                    
        if nums[start] == target or nums[end] == target:
            return True
        return False
            
    
    def existsInFirst(self, nums: List[int], start: int, target: int) -> bool:
        return nums[start] <= target
    
    
        
