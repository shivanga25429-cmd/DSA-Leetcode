class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = len(arr)
        n = len(arr)//2
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        arr = [[] for _ in range(len(arr)+1)]
        for ch , f in d.items():
            arr[f].append(ch)
        count = 0
        for i in range(len(arr)-1,0,-1):
            for j in arr[i]:
                l -= i
                count += 1
                if l<=n:
                    return count
            if l<=n:
                    return count
        if l<=n:
                    return count
