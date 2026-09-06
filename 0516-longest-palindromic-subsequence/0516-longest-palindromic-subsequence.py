class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        prev = [0]*(n+1)
        for i in range(1,n+1):
            curr = [0]*(n+1)
            for j in range(1,n+1):
                if s[i-1] == s[n-j]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        return prev[-1]



        