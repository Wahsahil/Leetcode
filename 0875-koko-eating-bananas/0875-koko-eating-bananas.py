import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/float(m))
            if hours <= h:
                r = m
            else:
                l = m + 1
        return l