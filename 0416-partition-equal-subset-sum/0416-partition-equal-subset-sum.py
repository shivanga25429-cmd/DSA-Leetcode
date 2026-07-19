class Solution(object):
    def canPartition(self, arr):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumi = sum(arr)
        m = len(arr)
        if sumi%2:
            return False
        n = sumi//2+1

        dp = []
        for i in range(m):
            arr2 = [False] * n
            dp.append(arr2)

        for i in range(m):
            dp[i][0] = True

        if arr[0] <= n:
            dp[0][arr[0]] = True

        for i in range(1, m):
            for j in range(1, n):
                not_take = dp[i - 1][j]
                take = False
                if j >= arr[i]:
                    take = dp[i - 1][j - arr[i]]
                dp[i][j] = take or not_take

        return dp[m - 1][sumi//2]