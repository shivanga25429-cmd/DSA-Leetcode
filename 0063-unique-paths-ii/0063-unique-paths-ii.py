class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return 0
        grid[0][0] = -1
        m = len(grid)
        n = len(grid[0])
        for i in range(1,n):
            if grid[0][i] == 1:
                grid[0][i] = 0
                continue
            else:
                grid[0][i] += grid[0][i-1]
        for i in range(1,m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    continue
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                grid[i][j] += grid[i-1][j]
        return -grid[-1][-1]