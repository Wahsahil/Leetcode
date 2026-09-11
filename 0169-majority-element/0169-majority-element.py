class Solution(object):
    def majorityElement(self, nums):
        h = {}
        for n in nums:
            h[n] = h.get(n,0) + 1
        max = 0
        maj = 0
        for i,j in h.items():
            if j>max:
                max = j
                maj =i
        return maj