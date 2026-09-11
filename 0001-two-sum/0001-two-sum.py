class Solution(object):
    def twoSum(self, nums, target):
        num = {}
        for i in range(len(nums)):
            n = target -nums[i]
            if n in num:
                return [num[n],i]
            num[nums[i]] = i

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        