class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        if not image or not image[0]:
            return 0
        
        m, n = len(image), len(image[0])
        # we can pass a function as a parameter of another function.
        left = self.binarySearch(image, 0, y, self.getColumnColor, '1')
        right = self.binarySearch(image, y, n - 1, self.getColumnColor, '0')
        top = self.binarySearch(image, 0, x, self.getRowColor, '1')
        down = self.binarySearch(image, x, m - 1, self.getRowColor, '0')
        
        return (right - left) * (down - top)
        
    def binarySearch(self, image, start, end, getColorFunc, color):
        while start + 1 < end:
            mid = (start + end) // 2
            if getColorFunc(image, mid) == color:
                end = mid
            else:
                start = mid
        if getColorFunc(image, start) == color:
            return start
        if getColorFunc(image, end) == color:
            return end
        return end + 1
      # If start and end do not give the 'color', end + 1 must give the 'color'!
    
    def getRowColor(self, image, index):
        for i in range(len(image[0])):
            if image[index][i] == '1':
                return '1'
        return '0'
    
    def getColumnColor(self, image, index):
        for i in range(len(image)):
            if image[i][index] == '1':
                return '1'
        return '0'
        
