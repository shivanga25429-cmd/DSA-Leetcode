class Solution(object):
    def minimumTotal(self, grid):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(grid)):
            grid[i][0] += grid[i-1][0]
            grid[i][-1] += grid[i-1][-1]
            for j in range(1,len(grid[i])-1):
                grid[i][j] = min(grid[i][j]+ grid[i-1][j], grid[i][j]+grid[i-1][j-1])
        return min(grid[-1])
        