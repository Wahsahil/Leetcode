class Solution(object):
    def maxSubArray(self, nums):
        cs = float('-inf')
        m = float('-inf')
        for i in range(len(nums)):
            cs = max(nums[i],cs+nums[i])
            m = max(cs,m)
        return m