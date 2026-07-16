class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(m):
            arr = [0]*n
            dp.append(arr)
        dp[0][0] = 1
        def backtrack(i,j):
            if dp[i][j]!=0:
                return dp[i][j]
            if i>0:
                dp[i][j] = dp[i][j]+backtrack(i-1,j)
            if j>0:
                dp[i][j] = dp[i][j]+backtrack(i,j-1)
            return dp[i][j]
        backtrack(m-1,n-1)
        return dp[m-1][n-1]
            