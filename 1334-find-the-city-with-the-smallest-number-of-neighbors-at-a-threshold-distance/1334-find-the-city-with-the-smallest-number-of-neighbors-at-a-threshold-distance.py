import heapq
class Solution(object):
    def findTheCity(self, n, edges, d):
        adj = [[] for _ in range(n)]
        ans , maxi = 0 , float('inf')
        for i in range(len(edges)):
            u , v , w = edges[i][0] , edges[i][1] , edges[i][2]
            adj[u].append((v , w))
            adj[v].append((u , w))
        for i in range(n):
            dist = [float('inf')] * n
            pq = []
            heapq.heappush(pq , (0 , i , 0))
            dist[i] = 0
            cnt = 0
            while pq:
                dis , node , wt = heapq.heappop(pq)
                if wt > dist[node] : continue
                if wt > d : continue
                cnt += 1
                for newn , newd in adj[node]:
                    if dist[newn] > newd + wt and newd + wt <= d:
                        dist[newn] = newd + wt
                        heapq.heappush(pq , (newd + wt , newn , dist[newn]))
            if cnt <= maxi:
                maxi = cnt
                ans = i
        return ans
                    

            
        
        