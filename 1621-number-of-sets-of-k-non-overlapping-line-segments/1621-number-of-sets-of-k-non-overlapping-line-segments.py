class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        prev = []
        for j in range(2):
            arr = [1]+[0]*(k)
            prev.append(arr)
        for ind in range(1,n+1):
            curr = []
            for j in range(2):
                arr = [1]+[0]*(k)
                curr.append(arr)
            for allow in range(2):
                for l in range(1,k+1):
                    if allow:
                        curr[allow][l] = max(curr[allow][l], curr[0][l-1] + prev[1][l])
                    else:
                        curr[allow][l] = max(curr[allow][l], prev[1][l]  + prev[0][l])
            prev = curr
        return (prev[0][-1])%(10**9+7)

            
        