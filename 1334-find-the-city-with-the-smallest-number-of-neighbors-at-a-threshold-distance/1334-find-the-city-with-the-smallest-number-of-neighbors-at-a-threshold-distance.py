class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dis = []
        for i in range(n):
            arr =[float("inf")]*n
            dis.append(arr)
        for i in range(n):
            dis[i][i] = 0
        for src,dst,weight in edges:
            dis[src][dst] = weight
            dis[dst][src] = weight
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j],dis[i][via]+ dis[via][j])
        mini = n
        i = n-1
        ans = n-1
        while i >=0:
            count = 0
            for j in range(n):
                if dis[i][j] <=distanceThreshold:
                    count += 1
            if count<mini:
                mini = count
                ans = i
            i -= 1
        return ans

        
        