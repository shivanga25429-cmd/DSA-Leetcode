class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp = []
        # for i in range(len(word1)):
        #     arr = [float("inf")]*len(word2)
        #     dp.append(arr)
        # def backtrack(i,j):
        #     if i==j==-1:
        #         return 0
        #     elif j <0:
        #         return i+1
        #     elif i<0:
        #         return j+1
        #     if dp[i][j]!=float("inf"):
        #         return dp[i][j]
        #     if word1[i] == word2[j]:
        #         dp[i][j] = backtrack(i-1,j-1)
        #     else:
        #         ins = 1 + backtrack(i,j-1)
        #         dele = 1 + backtrack(i-1,j)
        #         rep = 1 + backtrack(i-1,j-1)
        #         dp[i][j] = min(ins,dele,rep)
        #     return dp[i][j]
        # return backtrack(len(word1)-1,len(word2)-1)


        dp = []
        for i in range(len(word1)+1):
            arr = [float("inf")]*(len(word2)+1)
            dp.append(arr)
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(len(word1)+1):
            dp[i][0] = i
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    ins = 1 + dp[i][j-1]
                    dele = 1 + dp[i-1][j]
                    rep = 1 + dp[i-1][j-1]
                    dp[i][j] = min(ins,dele,rep)
        return dp[-1][-1]

        






        