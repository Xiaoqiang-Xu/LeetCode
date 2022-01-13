# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        elif reader.get(0) > target:
            return -1
        
        i = 1
        while reader.get(i) < target:
            i = 2 * i
        
        start, end = i // 2, i
        
        return self.binarySearch(reader, start, end, target)
    
    def binarySearch(self, reader, start, end, target):
        
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                end = mid
            else:
                start = mid
        
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
