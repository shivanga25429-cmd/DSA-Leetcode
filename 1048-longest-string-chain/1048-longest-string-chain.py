class Solution(object):
    def longestStrChain(self, words):
        n = len(words)
        dp = [1] * n

        words.sort(key=len)

        for i in range(n):
            for j in range(i):
                n1 = len(words[j])   # shorter
                n2 = len(words[i])   # longer

                if n1 + 1 == n2 and dp[i] < 1 + dp[j]:
                    check = True
                    valid = True
                    p = 0   # longer
                    q = 0   # shorter

                    while p < n2 and q < n1:
                        if words[i][p] != words[j][q]:
                            if check:
                                check = False
                                p += 1       # skip extra char
                            else:
                                valid = False
                                break
                        else:
                            p += 1
                            q += 1

                    if valid:
                        dp[i] = 1 + dp[j]

        return max(dp)