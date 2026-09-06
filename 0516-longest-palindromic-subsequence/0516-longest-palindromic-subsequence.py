class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = []
        n = len(s)
        for i in range(n+1):
            arr = [0]*(n+1)
            dp.append(arr)
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == s[n-j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]



        