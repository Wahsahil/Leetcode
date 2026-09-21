class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        c = 0
        for i in range(k):
            if blocks[i] == 'W':
                c += 1
        mc = c
        for i in range(k, n):
            if blocks[i-k] == 'W':
                c -= 1
            if blocks[i] == 'W':
                c += 1
            mc = min(mc, c)
        return mc