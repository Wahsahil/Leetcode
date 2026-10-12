class Solution(object):
    def intersection(self, nums1, nums2):
        h1 = set(nums1)
        h2 = set(nums2)
        return list(h1 & h2)
       
        
            

        