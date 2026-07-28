class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = []
        n = len(coins)
        for i in range(n):
            arr = [-1]*(amount+1)
            dp.append(arr)
        for i in range(amount +1):
            if i%coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = float("inf")
        
        for i in range(1,n):
            for j in range(amount+1):
                ntake = dp[i-1][j]
                take = float("inf")
                if coins[i]<=j:
                    take = 1 + dp[i][j-coins[i]]     
                dp[i][j] = min(take,ntake)

        if dp[n-1][amount] ==float("inf"):
            return -1
        return dp[n-1][amount]