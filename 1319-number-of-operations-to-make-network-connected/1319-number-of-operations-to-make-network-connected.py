class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n-1:
            return -1
        size = [1]*n
        parent = list(range(n))
        def find(ind):
            if parent[ind] == ind:
                return ind
            parent[ind] = find(parent[ind])
            return parent[ind]
        for i in connections:
            u = find(i[0])
            v = find(i[1])
            parent[u] = parent[v]
        s = set()
        for i in range(n):
            s.add(find(i))
        return len(s)-1