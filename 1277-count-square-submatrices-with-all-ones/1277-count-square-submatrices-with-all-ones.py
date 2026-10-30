class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        sumi = 0
        for j in range(m):
            dp[0][j] = matrix[0][j]
            sumi += dp[0][j]
        for i in range(1,n):
            dp[i][0] = matrix[i][0]
            sumi += dp[i][0]
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    sumi += dp[i][j]
        return sumi