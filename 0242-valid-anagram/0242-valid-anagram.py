class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        m = sorted(s)
        n = sorted(t)
        return m == n
        return True