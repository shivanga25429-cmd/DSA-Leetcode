class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return nums[0]
        maxi = nums[0]
        prev = nums[1]
        for i in range(2,n):
            curr = maxi + nums[i]
            maxi = max(maxi,prev)
            prev = curr
        return max(prev,maxi)