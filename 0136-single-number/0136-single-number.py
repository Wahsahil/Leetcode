class Solution(object):
    def singleNumber(self, nums):
       d ={}
       for i in nums:
            d[i] = d.get(i,0)+1
       for i in d:
        if d[i]==1:
            return i


        