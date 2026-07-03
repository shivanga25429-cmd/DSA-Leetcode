class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        import heapq
        ways = [0]*n
        ways[0] = 1
        pq = []
        adj = []
        dis = [float("inf")]*n
        for i in range(n):
            adj.append([])
        for fr,to,time in roads:
            adj[fr].append([to,time])
            adj[to].append([fr,time])
        heapq.heappush(pq,[0,0])
        dis[0] = 0
        while pq:
            time,curr = heapq.heappop(pq)
            if time > dis[curr]:
                continue
            for i in adj[curr]:
                newtime = i[1]+time
                if newtime< dis[i[0]]:
                    heapq.heappush(pq,[newtime,i[0]])
                    dis[i[0]] = newtime
                    ways[i[0]] = ways[curr]
                elif newtime == dis[i[0]]:
                    ways[i[0]] = (ways[i[0]]+ways[curr])%(10**9+7)

        return ways[n-1]



        