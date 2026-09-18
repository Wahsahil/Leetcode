class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        cz = 0
        for i in arr:
            if i ==0:
                cz+=1
        i = n-1
        j = n+cz-1
        while i<j:
            if j<n:
                arr[j]=arr[i]
            if arr[i]==0:
                j-=1
                if j<n:
                    arr[j]=0
            i -= 1
            j -= 1
