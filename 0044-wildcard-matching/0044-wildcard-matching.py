class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0

        # Position of the last '*'
        star = -1

        # Position in s where '*' started matching
        match = 0

        while i < len(s):

            # Normal character or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Found '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Mismatch, but we have a previous '*'
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Mismatch and no '*'
            else:
                return False

        # Remaining pattern must contain only '*'
        while j < len(p):
            if p[j] != '*':
                return False
            j += 1

        return True

        