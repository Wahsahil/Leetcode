class Solution:
    def isIsomorphic(self, s, t):
        h1 = {}
        h2 = {}
        for a, b in zip(s, t):
            if a in h1 and h1[a] != b:
                return False
            if b in h2 and h2[b] != a:
                return False
            h1[a] = b
            h2[b] = a
        return True