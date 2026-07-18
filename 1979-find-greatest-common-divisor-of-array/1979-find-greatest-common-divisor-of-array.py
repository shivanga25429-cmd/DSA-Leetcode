class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math
        mini = float("inf")
        maxi = float("-inf")
        for i in nums:
            mini = min(i,mini)
            maxi = max(i,maxi)
        return math.gcd(mini,maxi)
        