class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi = 0
        c = 0
        for i in s:
            if i =="(":
                c += 1
            elif i ==")":
                c -= 1
            maxi = max(maxi,c)
        return maxi