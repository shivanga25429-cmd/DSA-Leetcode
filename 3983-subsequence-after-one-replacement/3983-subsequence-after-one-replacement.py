class Solution(object):
    def canMakeSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n, m = len(s), len(t)
        
        # pre[i]: position in t matched for s[0..i-1], greedy earliest match
        pre = [0] * (n + 1)
        pre[0] = -1
        j = 0
        for i in range(1, n + 1):
            c = s[i - 1]
            while j < m and t[j] != c:
                j += 1
            if j == m:
                pre[i] = m  # fail -> stays m for all further i
            else:
                pre[i] = j
                j += 1
        
        # suf[i]: position in t matched for s[i..n-1], greedy latest match (from the right)
        suf = [0] * (n + 1)
        suf[n] = m
        jj = m - 1
        for i in range(n - 1, -1, -1):
            c = s[i]
            while jj >= 0 and t[jj] != c:
                jj -= 1
            if jj < 0:
                suf[i] = -1  # fail -> stays -1 for all further i
            else:
                suf[i] = jj
                jj -= 1
        
        # No replacement needed at all
        if pre[n] < m:
            return True
        
        # Try replacing each index i
        for i in range(n):
            if pre[i] < m and suf[i + 1] > -1 and suf[i + 1] - pre[i] >= 2:
                return True
        
        return False