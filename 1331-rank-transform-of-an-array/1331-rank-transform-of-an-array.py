class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorti = sorted(arr)
        dic = {}
        rank = 1
        for i in sorti:
            if i not in dic:
                dic[i] = rank
                rank += 1
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]
        return arr


