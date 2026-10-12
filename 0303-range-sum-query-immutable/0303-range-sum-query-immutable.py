class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1]+n)
        

    def sumRange(self, left, right):
        return self.prefix[right+1]-self.prefix[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)