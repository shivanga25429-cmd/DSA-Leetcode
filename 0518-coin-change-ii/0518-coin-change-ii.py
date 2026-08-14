class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        prev = [0]*(amount+1)
        for i in range(amount + 1):
            prev[i] += (i%coins[0] == 0)
            
        for i in range(1,len(coins)):
            curr = [0]*(amount+1)
            for j in range(amount+1):
                curr[j] += prev[j]
                if coins[i]<=j:
                    curr[j] += curr[j-coins[i]]
            prev = curr
                
        return prev[amount]