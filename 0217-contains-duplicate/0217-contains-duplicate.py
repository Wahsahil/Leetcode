class Solution(object):
    def containsDuplicate(self, nums):
        se = set()
        for n in nums:
            if n in se:
                return True
            se.add(n)
        return False
        