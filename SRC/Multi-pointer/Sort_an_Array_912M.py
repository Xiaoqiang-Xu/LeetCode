# Bubble sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        for i in range(n):
            indicator = 0
            for j in range(n - i -1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    indicator = 1
            if indicator == 0:
                return nums
            
        
# Selection sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        for i in range(n - 1):
            min_index = i
            for j in range(i, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        
        return nums
            
        
