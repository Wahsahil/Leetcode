class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h1 = {}
        h2 = {}
        ans = []
        for i in nums1:
            h1[i] = h1.get(i,0)+1
        for i in nums2:
            h2[i] = h2.get(i,0)+1
        for i in h1:
            if i in h2:
                ans.append(i)
        return ans 
        
            

        