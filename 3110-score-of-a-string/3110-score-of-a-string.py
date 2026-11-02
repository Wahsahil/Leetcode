class Solution(object):
    def scoreOfString(self, s):
        su =0
        f= 0
        for i in range(len(s)-1):
            f = abs((ord(s[i])-ord(s[i+1])))
            su= su+f
        return su
        