class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        ahead = [[0] * (k+1) for _ in range(2)]
        cur = [[0] * (k+1) for _ in range(2)]
        n = len(prices)
        # Iterate from the last day to the first day
        for ind in range(n - 1, -1, -1):
            for buy in range(2):  # 0 = buy possible, 1 = sell possible
                for cap in range(1, k+1):  # At most 2 transactions
                    if buy == 0:
                        # Option 1: Skip buying, Option 2: Buy stock
                        cur[buy][cap] = max(ahead[0][cap],
                                            -prices[ind] + ahead[1][cap])
                    else:
                        # Option 1: Skip selling, Option 2: Sell stock
                        cur[buy][cap] = max(ahead[1][cap],
                                            prices[ind] + ahead[0][cap - 1])
            # Move current state to ahead for the next iteration
            ahead = [row[:] for row in cur]

        return ahead[0][k]  # Maximum profit starting at day 0 with 2 transactions



