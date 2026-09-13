class Solution(object):
    def twoSum(self, nums, target):
        ans = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in ans:
                return [ans[n],i]
            ans[nums[i]]=i
    
        