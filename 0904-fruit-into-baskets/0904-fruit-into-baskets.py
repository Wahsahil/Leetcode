class Solution(object):
    def totalFruit(self, fruits):
        d = {}
        i = 0
        m = 0
        cf = 0
        for j in range(len(fruits)):
            d[fruits[j]] = d.get(fruits[j], 0) + 1
            while len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i += 1
            cf = j - i + 1
            m = max(cf, m)
        return m