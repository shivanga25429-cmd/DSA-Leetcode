class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev2 = 1
        prev = 1
        for i in range(2,n+1):
            curr = prev2 + prev
            prev2 = prev
            prev = curr
        if n<=1:
            return 1
        return curr
