class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        reach = 0
        count = 0
        maxi = 0
        for i in range(n):
            maxi = max(i + nums[i],maxi)
            if reach==i:
                count += 1
                reach = maxi
                if reach>=n-1:
                    return count
            
