class Solution(object):
    def subarraySum(self, nums, k):
        c = 0
        s = 0
        mp = {0: 1}
        for num in nums:
            s += num
            rem = s - k
            if rem in mp:
                c += mp[rem]
            mp[s] = mp.get(s, 0) + 1
        return c