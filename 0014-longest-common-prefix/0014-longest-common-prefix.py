class Solution:
    def longestCommonPrefix(self, strs):
        pre = strs[0]
        for i in strs[1:]:
            while  not i.startswith(pre):
                pre = pre[:-1]
            if pre =="":
                return ""
        return pre