class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        for i in s:
            st[i] = st.get(i,0)+1
        for i in range(len(s)):
            if st[s[i]]==1:
                return i
        return -1

        