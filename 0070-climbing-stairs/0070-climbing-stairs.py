class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev2 = 1
        prev = 1
        i = 2
        while i <n+1:
            curr = prev2 + prev
            prev2 = prev
            prev = curr
            i += 1
        if n<=1:
            return 1
        return curr
