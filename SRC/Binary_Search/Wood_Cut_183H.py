class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        n = len(L)
        if sum(L) < k:
            return 0
        
        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.piecesNumberAtLength(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self.piecesNumberAtLength(L, end) >= k:
            return end
        if self.piecesNumberAtLength(L, start) >= k:
            return start

    def piecesNumberAtLength(self, L, length):
        num_same_pieces = 0
        for i in L:
            num_same_pieces += i // length
        
        return num_same_pieces
