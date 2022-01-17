class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        # write your code here
        start, end = 1, min(times) * n
        while start + 1 < end:
            mid = (start + end) // 2
            if self.ok(n, times, mid):
                end = mid
            else:
                start = mid
        
        if self.ok(n, times, start):
            return start
        return end

    def ok(self, n, times, tm):
        num = 0
        for i in times:
            num += tm // i

        return n <= num
        
