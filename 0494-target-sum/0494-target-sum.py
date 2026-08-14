class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tsum = sum(nums)
        dp = []
        for _ in nums:
            arr = [-1]*(tsum+1)
            dp.append(arr)
        def backtrack(ind,sumi):
            if ind == len(nums):
                if 2*sumi - tsum == target:
                    return 1
                else:
                    return 0
            elif dp[ind][sumi] != -1:
                return dp[ind][sumi]
            pick = backtrack(ind+1,sumi+nums[ind])
            npick = backtrack(ind+1,sumi)
            dp[ind][sumi] = pick + npick
            return pick + npick
        return backtrack(0,0)


                
        

        