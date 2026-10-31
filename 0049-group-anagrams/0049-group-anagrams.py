class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in d:
                d[key].append(strs[i])
            else:
                d[key] = [strs[i]]
        return list(d.values())