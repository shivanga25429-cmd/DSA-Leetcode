class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        import heapq
        adj = []
        for i in range(n):
            adj.append([])
        for fr,to,price in flights:
            adj[fr].append([to,price])
        dis = [float("inf")]*n
        dis[src] = 0
        pq = []
        heapq.heappush(pq,[0,src,0])
        while pq:
            stops,curr,i = heapq.heappop(pq)
            if stops>k:
                continue
            for city,price in adj[curr]:
                new_price = i+price
                if new_price<dis[city]:
                    dis[city] = new_price
                    heapq.heappush(pq,[stops+1,city,new_price])
        if dis[dst] == float("inf"):
            return -1
        return dis[dst]


        

