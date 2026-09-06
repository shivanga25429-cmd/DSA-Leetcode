class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        rows = len(str1)
        cols = len(str2)
        dp =[]
        for i in range(rows+1):
            arr = [0]*(cols+1)
            dp.append(arr)
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        i = rows
        j = cols
        ans = []
        while i >0 and j>0:
            if str1[i-1] == str2[j-1]:
                ans.append(str1[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i-1][j]<=dp[i][j-1]:
                    ans.append(str2[j-1])
                    j -= 1
                else:
                    ans.append(str1[i-1])
                    i -= 1
        while i > 0:
            ans.append(str1[i-1])
            i -= 1

        while j > 0:
            ans.append(str2[j-1])
            j -= 1
        return "".join(ans[::-1])



        
        