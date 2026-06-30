class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque

        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        q = deque()
        q.append([0, 0])

        grid[0][0] = 1

        row = [1, -1, 0, 0, 1, 1, -1, -1]
        col = [0, 0, 1, -1, 1, -1, -1, 1]

        while q:
            curr = q.popleft()

            if curr[0] == n - 1 and curr[1] == n - 1:
                return grid[curr[0]][curr[1]]

            for k in range(8):
                i = curr[0] + row[k]
                j = curr[1] + col[k]

                if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                    grid[i][j] = grid[curr[0]][curr[1]] + 1
                    q.append([i, j])

        return -1