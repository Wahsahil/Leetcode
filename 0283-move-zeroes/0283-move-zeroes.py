class Solution(object):
    def moveZeroes(self, nums):
        r = []
        for i in range(len(nums)):
            if nums[i] != 0:
                r.append(nums[i])
        while len(r) < len(nums):
            r.append(0)
        nums[:] = r