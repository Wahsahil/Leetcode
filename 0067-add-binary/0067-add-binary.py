class Solution(object):
    def addBinary(self, a, b):
        n1 = int(a, 2)
        n2 = int(b, 2)
        total = n1 + n2
        return bin(total)[2:]