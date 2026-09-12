class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0

                if buy == 0:
                    profit = max(
                        0 + dp[ind + 1][0],
                        -prices[ind] + dp[ind + 1][1]
                    )

                if buy == 1:
                    profit = max(
                        0 + dp[ind + 1][1],
                        prices[ind] - fee + dp[ind + 1][0]
                    )

                dp[ind][buy] = profit

        return dp[0][0]
        