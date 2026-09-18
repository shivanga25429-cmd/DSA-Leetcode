class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = [1]*len(nums)
        dp = [1]*len(nums)
        maxi = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]+1>dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j]+1 == dp[i]:
                        count[i] += count[j]
            maxi = max(maxi,dp[i])
        cnt = 0
        for i in range(n):
            if dp[i] == maxi:
                cnt += count[i]
        return cnt
        

        