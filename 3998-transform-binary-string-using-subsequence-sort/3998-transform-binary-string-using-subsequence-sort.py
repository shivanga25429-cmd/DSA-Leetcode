class Solution(object):
    def transformStr(self, s, strs):
        """
        :type s: str
        :type strs: List[str]
        :rtype: List[bool]
        """
        arr = []
        ind = []

        for i in range(len(s)):
            if s[i] == "0":
                ind.append(i)

        zeros = len(ind)
        ones = len(s) - zeros

        for st in strs:
            zero = st.count("0")
            one = st.count("1")

            zero = zeros - zero
            one = ones - one

            l = list(st)

            for i in range(len(l)):
                if l[i] == "?":
                    if zero > 0:
                        l[i] = "0"
                        zero -= 1
                    else:
                        l[i] = "1"
                        one -= 1

            check = True

            if zero != 0 or one != 0:
                check = False
            else:
                i = 0
                for j in range(len(l)):
                    if l[j] == "0":
                        if j > ind[i]:
                            check = False
                            break
                        i += 1

            arr.append(check)

        return arr