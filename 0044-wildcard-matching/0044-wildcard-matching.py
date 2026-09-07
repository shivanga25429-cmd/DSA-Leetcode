class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp = []
        # for i in range(len(s)):
        #     arr = [None]*len(p)
        #     dp.append(arr)
        # def backtrack(i,j):
        #     if i ==j == -1:
        #         return True
        #     elif i<0 or j<0:
        #         return False
        #     if dp[i][j]!= None:
        #         return dp[i][j]
        #     if s[i] == p[j] or p[j] == "?":
        #         dp[i][j] =  backtrack(i-1,j-1)
        #     elif p[j] == "*":
        #         move = backtrack(i-1,j-1)
        #         nmove = backtrack(i-1,j)
        #         dmove = backtrack(i,j-1)
        #         dp[i][j] =  move or nmove or dmove
        #     else:
        #         dp[i][j] =  False
        #     return dp[i][j]
        # return backtrack(len(s)-1,len(p)-1)


        dp = []
        for i in range(len(s)+1):
            arr = [None]*(len(p)+1)
            arr[0] = False
            dp.append(arr)
        dp[0][0] = True
        for j in range(1,len(p)+1):
            dp[0][j] = dp[0][j-1] and p[j-1] == "*"
        

        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] =  dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] =  False
        return dp[-1][-1]

        