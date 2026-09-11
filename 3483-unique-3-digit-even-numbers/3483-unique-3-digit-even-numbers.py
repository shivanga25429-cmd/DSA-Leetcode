class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans = set()
        n = len(digits)
        used = [False]*len(digits)
        def backtrack(ind,no):
            if no//100 !=0:
                if no%2 == 0:
                    ans.add(no)
                return
            if ind>=n:
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    backtrack(ind+1,no*10+digits[i])
                    used[i] = False
        backtrack(0,0)
        return len(ans)


        