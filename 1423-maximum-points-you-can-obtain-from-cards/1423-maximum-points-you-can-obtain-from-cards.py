class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        cs = sum(cardPoints[:k])
        ms = cs
        for i in range(1, k + 1):
            cs = cs - cardPoints[k-i] + cardPoints[n-i]
            ms = max(ms, cs)

        return ms