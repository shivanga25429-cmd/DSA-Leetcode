class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        arr = []
        l = len(str(low))
        seq = "123456789"
        upper = len(str(high))+1
        while l<upper:
            i = 0
            j = i+l
            while j<10:
                x = int(seq[i:j])
                if low<=x<=high:
                    arr.append(x)
                i += 1
                j += 1
            l += 1
            if x > high:
                break
        return arr

        