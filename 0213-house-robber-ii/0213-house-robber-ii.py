class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n<=2:
            return max(nums)
        maxi = nums[0]
        prev = nums[1]
        for i in range(2,n-1):
            curr = maxi + nums[i]
            maxi = max(maxi,prev)
            prev = curr
        maxi = max(prev,maxi)

        maxi2 = nums[1]
        prev = nums[2]
        for i in range(3,n):
            curr = maxi2 + nums[i]
            maxi2 = max(maxi2,prev)
            prev = curr
        maxi2 =  max(prev,maxi2)
        return max(maxi,maxi2)