class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word2)
        prev = [0]*(n+1)
        for i in range(1,len(word1)+1):
            curr = [0]*(n+1)
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr
        return (len(word1)+n)- 2*prev[-1]