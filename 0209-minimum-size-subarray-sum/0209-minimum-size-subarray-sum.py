class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = 0
        s = 0
        m = float('inf')
        for j in range(0,len(nums)):
            s = s + nums[j]
            while s >= target:
                l = j - i + 1
                m = min(m, l)
                s = s - nums[i]
                i += 1
        if m == float('inf'):
            return 0
        return m