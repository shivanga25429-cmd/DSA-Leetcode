class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev = []
        for j in range(len(word2)+1):
            prev.append(j)
        for i in range(1,len(word1)+1):
            curr = [float("inf")]*(len(word2)+1)
            curr[0] = i
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    ins = 1 + curr[j-1]
                    dele = 1 + prev[j]
                    rep = 1 + prev[j-1]
                    curr[j] = min(ins,dele,rep)
            prev = curr
        return prev[-1]

        






        