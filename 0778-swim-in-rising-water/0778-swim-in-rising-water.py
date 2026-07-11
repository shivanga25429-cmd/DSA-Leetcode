class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dis = []
        for _ in range(n):
            dis.append([float("inf")]*n)
        dis[0][0] = grid[0][0]
        import heapq
        pq = []
        heapq.heappush(pq,[grid[0][0],0,0])
        while pq:
            maxi,i,j = heapq.heappop(pq)
            if i == j == n-1:
                return maxi
            if maxi>dis[i][j]:
                continue
            if i<n-1 and dis[i+1][j] > max(maxi,grid[i+1][j]):
                dis[i+1][j] = max(maxi,grid[i+1][j])
                heapq.heappush(pq,[max(maxi,grid[i+1][j]),i+1,j])
            if j<n-1 and dis[i][j+1] > max(maxi,grid[i][j+1]):
                dis[i][j+1] = max(maxi,grid[i][j+1])
                heapq.heappush(pq,[max(maxi,grid[i][j+1]),i,j+1])
            if i>0 and dis[i-1][j] > max(maxi,grid[i-1][j]):
                dis[i-1][j] = max(maxi,grid[i-1][j])
                heapq.heappush(pq,[max(maxi,grid[i-1][j]),i-1,j])
            if j>0 and dis[i][j-1] > max(maxi,grid[i][j-1]):
                dis[i][j-1] = max(maxi,grid[i][j-1])
                heapq.heappush(pq,[max(maxi,grid[i][j-1]),i,j-1])
        
                