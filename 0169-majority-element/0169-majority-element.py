class Solution(object):
    def majorityElement(self, nums):
        d ={}
        m=0
        mj=0
        for i in nums:
            d[i] = d.get(i,0)+1
        for i in d:
            if d[i]>m:
                m= d[i]
                mj=i
        return mj