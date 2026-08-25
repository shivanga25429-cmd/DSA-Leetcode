class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        t = k
        for i in nums:
            if t == i:
                t += k
            elif t<i:
                return t
        return t
        