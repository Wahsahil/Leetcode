class Solution(object):
    def countCommas(self, n):
        count = 0
        x = 1000

        while x <= n:
            count += n - x + 1
            x *= 1000

        return count