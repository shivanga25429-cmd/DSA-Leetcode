class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp = [1]*n
        h = list(range(n))
        ind = 0
        nums.sort()
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and nums[i]%nums[j] ==0:
                    if dp[j]+1>dp[i]:
                        dp[i] = dp[j]+1
                        h[i] = j
            if dp[i]>dp[ind]:
                ind = i
        arr =[]
        while h[ind]!=ind:
            arr.append(nums[ind])
            ind = h[ind]
        arr.append(nums[ind])
        return arr



        

            
        