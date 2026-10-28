class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        reach = 0
        i = 0
        arr = []
        count = 0
        for i in range(len(s)):
            reach = max(reach,dic[s[i]])
            count += 1
            if reach == i:
                arr.append(count)
                count = 0
                reach = 0
        return arr

