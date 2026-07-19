class Solution(object):
    def minimumGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def min_rotation(s):
            ss = s+s
            i = 0
            j = 1
            k = 0
            while i<len(s) and j <len(s) and k <len(s):
                if ss[i+k] == ss[j+k]:
                    k += 1
                    continue
                if ss[i+k] > ss[j+k]:
                    i = i + k + 1
                    if i <= j:
                        i = j + 1
                else:
                    j += k + 1
                    if j<=i:
                        j = i+1
                k = 0
            ind = min(i,j)
            return ss[ind:ind+len(s)]
        groups = set()
        for i in words:
            groups.add(min_rotation(i[::2])+min_rotation(i[1::2]))
        return len(groups)
            
                
                
        