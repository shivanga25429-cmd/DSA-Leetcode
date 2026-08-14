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
        prev = [0]*(tsum+1)
        prev[0] += 1
        prev[nums[0]] += 1
        rtarget = (target+tsum)//2
        for i in range(1,len(nums)):
            for j in range(tsum,nums[i]-1,-1):
                prev[j] += prev[j-nums[i]]          
        return prev[rtarget]

        



        


                
        

        