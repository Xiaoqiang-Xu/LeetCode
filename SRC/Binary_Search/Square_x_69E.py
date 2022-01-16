class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 1, x
        
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid
            else:
                start = mid
                
        if end * end <= x:
            return end
        if start * start <= x:
            return start
        
        
