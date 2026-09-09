class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 999
        ans = 0
        while n>temp:
            ans += (n-temp)
            temp = temp*1000+999
        return ans