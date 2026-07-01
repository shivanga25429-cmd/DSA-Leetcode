class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        from collections import deque
        dis = [float("inf")]*(n+1)
        dis[k] = 0
        dis[0] = 0
        adj=[]
        for i in range(n+1):
            adj.append([])
        for src,dst,time in times:
            adj[src].append([dst,time])
        q = deque()
        q.append([k,0])
        while q:
            dst,time = q.popleft()
            for i,j in adj[dst]:
                if time+j<dis[i]:
                    dis[i] = time+j
                    q.append([i,time+j])
        maxi = max(dis)
        if maxi == float("inf"):
            return -1
        return maxi



        