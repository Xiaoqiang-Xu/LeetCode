class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]

        
        
        
    def findBound(self, nums: list[int], target: int, isFirst: bool) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if isFirst:
                    end = mid
                else:
                    start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if isFirst:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
        else:
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start
            
        
        return -1
                
            
                
            
        
        
