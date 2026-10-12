class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                if i!=j:
                    nums[i],nums[j] = nums[j],nums[i]
                j+=1