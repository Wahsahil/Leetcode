class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        n = len(arr)
        c=0
        cs = sum(arr[:k])  
        if cs//k>=threshold:
            c+=1   
        for i in range(k,n):
            cs = cs+arr[i]
            cs = cs-arr[i-k]
            if cs//k>=threshold:
                c+=1
        return c
        