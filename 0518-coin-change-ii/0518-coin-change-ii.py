class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = []
        for i in coins:
            arr = [-1]*(amount + 1)
            dp.append(arr)
        dp[0][0] = 1
        def backtrack(ind,target):
            if ind<0:
                if target==0:
                    return 1
                return 0
            if dp[ind][target] != -1:
                return dp[ind][target]
            npick = backtrack(ind-1,target)
            pick = 0
            if coins[ind]<=target:
                pick = backtrack(ind,target-coins[ind])
            dp[ind][target] = pick + npick
            return dp[ind][target]
        backtrack(len(coins)-1,amount)
        return dp[-1][amount]