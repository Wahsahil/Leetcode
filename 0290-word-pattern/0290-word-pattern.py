class Solution(object):
    def wordPattern(self, pattern, s):
        h1 = {}
        h2 = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for a,b in zip(pattern,words):
            if a in h1 and h1[a]!=b:
                return False
            if b in h2 and h2[b]!=a:
                return False
            h1[a] = b
            h2[b] = a
        return True
        