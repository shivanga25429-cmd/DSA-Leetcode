class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        op = 1
        cost = k
        ans = 0
        for x in nums:
            if x > cost:
                need = x - cost
                m = (need + k - 1) // k  
                ans += m * (2 * op + m - 1) // 2
                ans %= MOD
                op += m
                cost += m * k
            cost -= x
        return int(ans % MOD)