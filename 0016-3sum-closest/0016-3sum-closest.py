class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float("inf")
        sumi = 0
        l = len(nums)
        for i in range(l-2):
            j = i+1
            k = l-1
            while j <k:
                add = nums[i]+nums[j]+nums[k]
                dif = abs(add-target)
                if dif<diff:
                    sumi = add
                    diff = dif
                if add<=target:
                    j += 1
                else:
                    k -= 1
        return sumi

        