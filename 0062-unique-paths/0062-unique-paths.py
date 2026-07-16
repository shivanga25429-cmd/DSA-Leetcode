class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0]*n
        dp[0] = 1
        for i in range(m):
            for i in range(1,n):
                dp[i] = dp[i]+dp[i-1]
        return dp[-1]

            