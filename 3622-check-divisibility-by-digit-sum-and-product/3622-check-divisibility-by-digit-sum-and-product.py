class Solution(object):
    def checkDivisibility(self, n):
        s=0
        p=1
        t=n
        while t>0:
            s=s+t%10
            p=p*(t%10)
            t=t//10
        s=s+p
        if n%s==0:
            return True
        else:
            return False
            
        
        