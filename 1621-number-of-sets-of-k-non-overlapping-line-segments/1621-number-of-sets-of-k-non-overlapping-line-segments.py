class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = []
        for i in range(n+1):
            dp.append([])
            for j in range(2):
                arr = [1]+[0]*(k)
                dp[i].append(arr)
        for ind in range(1,n+1):
            for allow in range(2):
                for l in range(1,k+1):
                    if allow:
                        dp[ind][allow][l] = max(dp[ind][allow][l], dp[ind][0][l-1] + dp[ind-1][1][l])
                    else:
                        dp[ind][allow][l] = max(dp[ind][allow][l], dp[ind-1][1][l]  + dp[ind-1][0][l])
        return (dp[-1][0][-1])%(10**9+7)

            
        