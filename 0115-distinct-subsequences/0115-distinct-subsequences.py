class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = []
        for i in range(len(s)+1):
            arr = [0]*(len(t)+1)
            dp.append(arr)

        for i in range(len(s)):
            dp[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                dp[i][j] += dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[-1][-1]
