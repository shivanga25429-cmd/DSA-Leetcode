class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        stk = []
        for i in num:
            while stk and k and stk[-1] > i:
                stk.pop()
                k -= 1
            stk.append(i)
        for i in range(k):
            stk.pop()
        i = 0
        while i < len(stk) - 1:
            if stk[i] == "0":
                i+=1
            else:
                break
        if stk:
            return ''.join(stk[i:])
        return "0"
