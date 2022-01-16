class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        if x >= 1:
            start, end = 1, x
        if x < 1:
            start, end = x, 1

        while start + 1e-12 < end:
            mid = (start + end) / 2
            if mid * mid < x:
                start = mid
            else:
                end = mid
        
        if end * end <= x:
            return end
        if start * start <= x:
            return start
