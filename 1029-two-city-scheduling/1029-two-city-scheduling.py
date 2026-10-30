class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key =lambda x: x[0]-x[1])
        i = 0
        j = len(costs)- 1
        ans = 0
        while i<j:
            ans += costs[i][0] + costs[j][1]
            i += 1
            j -= 1
        return ans

        