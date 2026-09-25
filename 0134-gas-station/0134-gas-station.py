class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        s=0
        t=0
        ta=0
        for i in range(len(gas)):
             t +=  gas[i]-cost[i]
             ta+= gas[i]-cost[i]
             if ta<0:
                s=i+1
                ta =0
        if t<0:
            return -1
        else:
            return s
        