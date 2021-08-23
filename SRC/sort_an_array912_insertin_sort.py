class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            v = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > v:
                nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = v
        return nums
