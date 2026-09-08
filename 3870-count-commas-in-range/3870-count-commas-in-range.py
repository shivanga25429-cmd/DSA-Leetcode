class Solution(object):
    def countCommas(self, n):
        if n<1000:
            return 0
        elif 10**5>n>=1000:
            return n-1000+1
        else:
            return 99001

        