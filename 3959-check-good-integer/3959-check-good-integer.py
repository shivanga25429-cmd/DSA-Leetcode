class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum1 = 0
        sum2 = 0
        while n > 0:
            x = n%10
            sum1 += x
            sum2 += x*x
            n = n//10
        if sum2-sum1>=50:
            return True
        return False