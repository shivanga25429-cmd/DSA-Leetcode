
class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]

        def solve(i, j1, j2):

            # Out of bounds
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')

            # Base case: last row
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                return grid[i][j1] + grid[i][j2]

            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            # Collect current row cherries
            cherries = grid[i][j1]

            if j1 != j2:
                cherries += grid[i][j2]

            maxi = float('-inf')

            # Try all 9 combinations
            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:

                    val = solve(i + 1, j1 + d1, j2 + d2)

                    maxi = max(maxi, val)

            dp[i][j1][j2] = cherries + maxi

            return dp[i][j1][j2]

        return solve(0, 0, m - 1)
