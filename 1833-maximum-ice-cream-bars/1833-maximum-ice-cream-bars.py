class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        freq = [0] * (max(costs) + 1)
        for c in costs:
            freq[c] += 1

        bars = 0
        for price in range(1, len(freq)):
            if freq[price] == 0:
                continue
            if coins < price:
                break
            count = min(freq[price], coins // price)
            bars += count
            coins -= count * price
        return bars
            
