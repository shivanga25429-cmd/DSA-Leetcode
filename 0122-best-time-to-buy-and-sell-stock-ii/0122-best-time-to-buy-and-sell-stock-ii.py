class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = []
        for i in range(len(prices)+1):
            dp.append([0,0])
        # def backtrack(i,buy):
        #     if i == len(prices)-1:
        #         if buy:
        #             dp[i][buy] = 0
        #             return dp[i][buy]
        #         dp[i][buy] = prices[i]
        #         return dp[i][buy]
        #     if dp[i][buy]!=-1:
        #         return dp[i][buy]
        #     if buy:
        #         dp[i][buy]=max(-prices[i]+backtrack(i+1,0), backtrack(i+1,1))    
        #     else:
        #         dp[i][buy]=max(prices[i]+backtrack(i+1,1), backtrack(i+1,0))
        #     return dp[i][buy]
                
        # return backtrack(0,1)
        for i in range(len(prices)-1,-1,-1):
            for j in range(2):
                if j:
                    dp[i][j]=max(-prices[i]+dp[i+1][0], dp[i+1][1])    
                else:
                    dp[i][j]=max(prices[i]+dp[i+1][1], dp[i+1][0])
        return dp[0][1]
        


