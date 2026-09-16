class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        c= 1
        for i in range(1,n+k):
            c = c*i
        den1 = 1
        for j in range(1,2*k+1):
            den1 = den1*j
        den2 = 1
        for l in range(1,n-k):
            den2 = den2*l
        return (c//(den1*den2))%(10**9+7)

            
        