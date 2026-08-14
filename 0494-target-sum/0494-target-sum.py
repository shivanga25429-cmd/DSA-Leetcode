class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        tsum = sum(nums)
        if tsum-abs(target)<0 or (target+tsum)%2 != 0:
            return 0
        dp = []
        for _ in nums:
            arr = [0]*(tsum+1)
            dp.append(arr)
        dp[0][0] += 1
        dp[0][nums[0]] += 1
        rtarget = (target+tsum)//2
        for i in range(1,len(nums)):
            for j in range(tsum+1):
                dp[i][j] += dp[i-1][j]
                if nums[i]<=j:
                    dp[i][j] += dp[i-1][j-nums[i]]
        return dp[-1][rtarget]


        


                
        

        