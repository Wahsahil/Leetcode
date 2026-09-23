class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) ==0:
            return 0
        i = 0
        win = set()
        m = float('-inf')
        for j in range(len(s)):
            while s[j] in win:
                win.remove(s[i])
                i+=1 
            win.add(s[j])
            l = j-i+1
            m = max(m,l)
        return m
        