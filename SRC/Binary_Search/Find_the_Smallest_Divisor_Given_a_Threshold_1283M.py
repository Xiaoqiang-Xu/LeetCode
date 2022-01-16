class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        start, end = 1, max(nums)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.divisorSum(nums, mid) > threshold:
                start = mid
            else:
                end = mid
        if self.divisorSum(nums, start) <= threshold:
            return start
        if self.divisorSum(nums, end) <= threshold:
            return end
            
            
    def divisorSum(self, nums, divisor):
        sum = 0
        for i in nums:
            sum += math.ceil(i / divisor)
            
        return sum
        
