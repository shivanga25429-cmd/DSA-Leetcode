from collections import defaultdict
import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #minimum time to reach the destination
        time=[float('inf') for i in range(n+1)]
        time[k]=0
        heap=[(0,k)]
        graph=defaultdict(list)
        for i,j,w in times:
            graph[i].append((j,w))
        # seee we need the heap cause of weig
        while heap:
            currtime,node=heapq.heappop(heap)
            #this implies
            #starting from somewhere and if i reached here it means this 
            if currtime>time[node]:
                continue
            for adj,weight in graph[node]:
                if time[adj]>currtime+weight:
                    time[adj]=currtime+weight
                    heapq.heappush(heap,(currtime+weight,adj))
        maxi=float('-inf')
        for i in range(1,len(time)):
            if time[i]==float('inf'):
                return -1
            maxi=max(maxi,time[i])
        return maxi

        