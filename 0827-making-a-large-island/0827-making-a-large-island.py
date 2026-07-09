class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        parent = list(range(n * n))
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

                u = n * i + j

                if i < n - 1 and grid[i + 1][j]:
                    ru = find(u)
                    rv = find(u + n)
                    if ru != rv:
                        if size[ru] <= size[rv]:
                            size[rv] += size[ru]
                            parent[ru] = rv
                        else:
                            size[ru] += size[rv]
                            parent[rv] = ru

                if j < n - 1 and grid[i][j + 1]:
                    ru = find(u)
                    rv = find(u + 1)
                    if ru != rv:
                        if size[ru] <= size[rv]:
                            size[rv] += size[ru]
                            parent[ru] = rv
                        else:
                            size[ru] += size[rv]
                            parent[rv] = ru

        maxi = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    continue
                u = n * i + j
                unique = set()
                if i > 0 and grid[i - 1][j]:
                    unique.add(find(u - n))
                if j > 0 and grid[i][j - 1]:
                    unique.add(find(u - 1))
                if i < n - 1 and grid[i + 1][j]:
                    unique.add(find(u + n))
                if j < n - 1 and grid[i][j + 1]:
                    unique.add(find(u + 1))
                area = 1
                for k in unique:
                    area += size[k]
                maxi = max(maxi, area)
        if not maxi:
            return n*n
        return maxi