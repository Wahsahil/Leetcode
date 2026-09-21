class Solution(object):
    def maxVowels(self, s, k):
        n = len(s)
        vowels = "aeiou"
        c = 0
        for i in range(k):
            if s[i] in vowels:
                c += 1
        ms = c
        for i in range(k,n):
            if s[i-k] in vowels:
                c-=1
            if s[i] in vowels:
                c+=1
            ms = max(c,ms)
        return ms
            
                   

        