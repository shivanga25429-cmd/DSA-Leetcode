class Solution(object):
    def filterOccupiedIntervals(self, occupiedIntervals, freeStart, freeEnd):
        """
        :type occupiedIntervals: List[List[int]]
        :type freeStart: int
        :type freeEnd: int
        :rtype: List[List[int]]
        """
        occupiedIntervals.sort()
        stk = []
        stk.append(occupiedIntervals[0])

        for i in range(1, len(occupiedIntervals)):
            if stk[-1][1] + 1 >= occupiedIntervals[i][0]:
                stk[-1][1] = max(stk[-1][1], occupiedIntervals[i][1])
            else:
                stk.append(occupiedIntervals[i])
        arr = []

        
        for i in stk:
            if i[0] >= freeStart and i[1] <= freeEnd:
                continue
        
            elif i[0] < freeStart and i[1] >= freeStart and i[1] <= freeEnd:
                arr.append([i[0], freeStart - 1])
        
            elif i[0] >= freeStart and i[0] <= freeEnd and i[1] > freeEnd:
                arr.append([freeEnd + 1, i[1]])
        
            elif i[0] < freeStart and i[1] > freeEnd:
                arr.append([i[0], freeStart - 1])
                arr.append([freeEnd + 1, i[1]])
        
            # No overlap
            else:
                arr.append(i)

        return arr