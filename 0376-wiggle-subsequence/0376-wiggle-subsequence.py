class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1:
            return 1
        
        ans = 1
        prev = 0
        
        for i in range(1, n):
            curr = nums[i] - nums[i-1]
            
            if curr > 0 and prev <= 0:
                ans += 1
                prev = curr
                
            elif curr < 0 and prev >= 0:
                ans += 1
                prev = curr
                
        return ans
