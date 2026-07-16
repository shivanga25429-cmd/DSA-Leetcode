class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        prev = [grid[0][0]]
        for i in range(1,n):
            prev.append(grid[0][i] + prev[i-1])
        for i in range(1,m):
            curr = [0]*n
            for j in range(n):
                x = float("inf")
                if j>0:
                    x = grid[i][j] + curr[j-1]
                y = grid[i][j] + prev[j]
                curr[j] = min(x,y)
            prev = curr[::]
        return prev[-1]
        
