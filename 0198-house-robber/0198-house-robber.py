class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        if n==1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = nums[1]
        maxi = dp[0]
        for i in range(2,n):
            dp[i] = maxi + nums[i]
            maxi = max(maxi,dp[i-1])
        return max(dp[-1],maxi)