class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        seti = set(wordDict)
        dp = []
        for i in range(len(s)):
            arr = [None]*len(s)
            dp.append(arr)
        def backtrack(i,j):
            if j>=len(s):
                if i == j:
                    return True
                elif s[i:j] not in seti:
                    return False
                return True
            if dp[i][j]!=None:
                return dp[i][j]
            if s[i:j+1] in seti:
                dp[i][j] = backtrack(j+1,j+1)
            dp[i][j] = dp[i][j] or backtrack(i,j+1)
            return dp[i][j]
        return backtrack(0,0)
        