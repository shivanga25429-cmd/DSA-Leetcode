class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        prev = [0]*(len(t)+1)
        prev[0] = 1
        for i in range(1,len(s)+1):
            if prev[0]!= 1:
                prev[0] = 1
            curr = [0]*(len(t)+1)
            for j in range(1,len(t)+1):
                curr[j] += prev[j]
                if s[i-1] == t[j-1]:
                    curr[j] += prev[j-1]
            prev = curr
        return prev[-1]
