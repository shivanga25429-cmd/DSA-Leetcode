class Solution(object):
    def minCost(self, n, cuts):

        cuts.sort()
        arr = [0] + cuts + [n]

        m = len(arr)

        dp = [[-1] * m for _ in range(m)]

        def backtrack(i, j):

            # No cut exists between i and j
            if j - i <= 1:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            mini = float("inf")

            for k in range(i + 1, j):

                cost = (
                    arr[j] - arr[i]
                    + backtrack(i, k)
                    + backtrack(k, j)
                )

                mini = min(mini, cost)

            dp[i][j] = mini
            return mini

        return backtrack(0, m - 1)