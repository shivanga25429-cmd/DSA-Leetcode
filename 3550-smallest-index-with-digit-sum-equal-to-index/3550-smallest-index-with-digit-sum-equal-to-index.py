class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            s = 0
            temp = nums[i]
            while temp:
                s += temp%10
                temp//= 10
            if i == s:
                return i
        return -1