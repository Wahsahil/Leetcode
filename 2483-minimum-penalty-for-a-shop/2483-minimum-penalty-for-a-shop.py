class Solution(object):
    def bestClosingTime(self, customers):
        p = customers.count('Y')
        mp = p
        ans = 0
        for i in range(len(customers)):
            if customers[i]=='Y':
                p-=1
            else:
                p+=1
            if p<mp:
                mp=p
                ans = i+1
        return ans
        