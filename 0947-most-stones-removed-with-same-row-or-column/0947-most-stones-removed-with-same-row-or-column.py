class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        dic = {}
        def find(node):
            if node not in dic:
                dic[node] = node
            if dic[node] == node:
                return node
            dic[node] = find(dic[node])
            return dic[node]
        
        for i in stones:
            u = find(i[0])
            v = find(i[1]+10001)
            dic[u] = v
        s = set()
        for i in dic:
            s.add(find(i))
        return n-len(s)
        

            