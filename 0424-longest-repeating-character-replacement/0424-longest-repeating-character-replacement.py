class Solution(object):
    def characterReplacement(self, s, k):
            f = {}
            i = 0 
            l = 0
            for j in range(len(s)):
                f[s[j]] = f.get(s[j],0)+1
                mf = max(f.values())
                while(j-i+1)-mf > k:
                    f[s[i]]-=1
                    i+=1
                   
                l = max(l,j-i+1)
            return l
 

        