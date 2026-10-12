class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        t = sum(range(n+1))
        for i in nums:
            t -=i
        return t
        