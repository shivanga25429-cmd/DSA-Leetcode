class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        vis = [False]*n
        low = [float("inf")]*n
        tin = [0]*n
        self.timer = 0
        adj = []
        ans = []
        for i in range(n):
            adj.append([])
        for i in connections:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        def dfs(node, parent):
            vis[node] = True
            tin[node] = low[node] = self.timer
            self.timer += 1
            for i in adj[node]:
                if i == parent:
                    continue
                if vis[i]:
                    low[node] = min(low[node], low[i])
                else:
                    dfs(i,node)
                    low[node] = min(low[node], low[i])
                    if low[i] > tin[node]:
                        ans.append([i,node])
        dfs (0,None)
        return ans
                    






        