class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        temp = 999
        ans = 0
        while n>temp:
            ans += (n-temp)
            i+=1
            temp = temp*1000+999
        return ans