class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = nums[0]
        prefix = nums[:]
        for i in range(len(nums)):
            maxi = max(prefix[i],maxi)
            prefix[i] = maxi
        for i in range(len(nums)):
            prefix[i] = math.gcd(nums[i],prefix[i])
        prefix.sort()
        sumi = 0
        i = 0
        j = len(prefix) - 1
        while i < j:
            sumi += gcd(prefix[i],prefix[j])
            i += 1
            j -= 1
        return sumi
        