class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        n = len(pages)
        if k >= n:
            return max(pages)
        
        # The shortest time will be in the range of max(pages) to sum(pages).
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.getLeastPeople(pages, mid) > k:
                start = mid
            else:
                end = mid

        if self.getLeastPeople(pages, start) <= k:
            return start
        return end

    def getLeastPeople(self, pages, time_limit):
        count = 0
        time_cost = 0
        for i in pages:
            if time_cost + i > time_limit:
                count += 1
                time_cost = 0
            time_cost += i
        
        return count + 1

        


