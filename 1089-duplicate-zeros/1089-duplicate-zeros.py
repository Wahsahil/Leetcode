
class Solution(object):
    def duplicateZeros(self, arr):
        ans = []
        for i in range(len(arr)):
            if arr[i] == 0:
                ans.append(0)
                ans.append(0)
            else:
                ans.append(arr[i])
        arr[:] = ans[:len(arr)]