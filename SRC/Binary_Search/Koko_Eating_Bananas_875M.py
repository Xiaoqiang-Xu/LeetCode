import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        speed_start = 1
        speed_end = max(piles)
        
        while speed_start + 1 < speed_end:
            mid = (speed_start + speed_end) // 2
            if self.hoursAtSpeed(piles, mid) > h:
                speed_start = mid
            else:
                speed_end = mid
        if self.hoursAtSpeed(piles, speed_start) <= h:
            return speed_start
        if self.hoursAtSpeed(piles, speed_end) <= h:
            return speed_end
            
    def hoursAtSpeed(self, piles, speed):
        hours = 0
        for i in piles:
            hours += math.ceil(i / speed)
            
        return hours
            
            
