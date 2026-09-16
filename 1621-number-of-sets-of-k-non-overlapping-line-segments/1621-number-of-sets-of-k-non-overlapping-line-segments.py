class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = []
        for i in range(n):
            dp.append([])
            for j in range(2):
                arr = [-1]*(k+1)
                dp[i].append(arr)
        def backtrack(ind,allow,l):
            if l ==0:
                return 1
            if ind==n:
                return 0
            if dp[ind][allow][l]!=-1:
                return dp[ind][allow][l]
            if allow:
                dp[ind][allow][l] = max(dp[ind][allow][l], backtrack(ind+1,0,l) + backtrack(ind+1,1,l))
            else:
                dp[ind][allow][l] = max(dp[ind][allow][l], backtrack(ind,1,l-1)  + backtrack(ind+1,0,l))
            return dp[ind][allow][l]
        return backtrack(0,1,k)%(10**9+7)
            
        