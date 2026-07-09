class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        parent = list(range(n*n))
        size = []
        for i in range(n):
            for j in range(n):
                size.append(grid[i][j])

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    continue

                u = n*i + j

                if i < n-1 and grid[i+1][j] and find(u) != find(u+n):
                    if size[find(u)] <= size[find(u+n)]:
                        size[find(u+n)] += size[find(u)]
                        parent[find(u)] = find(u+n)
                    else:
                        size[find(u)] += size[find(u+n)]
                        parent[find(u+n)] = find(u)

                if j < n-1 and grid[i][j+1] and find(u) != find(u+1):
                    if size[find(u)] <= size[find(u+1)]:
                        size[find(u+1)] += size[find(u)]
                        parent[find(u)] = find(u+1)
                    else:
                        size[find(u)] += size[find(u+1)]
                        parent[find(u+1)] = find(u)

        maxi = max(size)

        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    u = n*i + j
                    unique = set()

                    if i > 0 and grid[i-1][j]:
                        unique.add(find(u-n))
                    if j > 0 and grid[i][j-1]:
                        unique.add(find(u-1))
                    if i < n-1 and grid[i+1][j]:
                        unique.add(find(u+n))
                    if j < n-1 and grid[i][j+1]:
                        unique.add(find(u+1))

                    area = 1
                    for k in unique:
                        area += size[k]
                    maxi = max(maxi, area)

        return maxi