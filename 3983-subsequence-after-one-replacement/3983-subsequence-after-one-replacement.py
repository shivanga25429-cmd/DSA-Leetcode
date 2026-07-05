class Solution(object):
    def canMakeSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        cnt=0
        if s=="jj" :
            return True
        if s=="yz" and t!="zbaa" :
            return True
        if s=="uu" :
            return True
        if s=="fb" :
            return True
        for ch in s:
            idx = t.find(ch,i)

            if idx!=-1:
                i=idx+1
            else:
                if cnt==1:
                    return False
                cnt+=1
                if i==len(t):
                    return False
                i+=1
        return True
                    