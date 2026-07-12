class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        st = startTime.split(":")
        en = endTime.split(":")
        sec = (int(en[0])-int(st[0]))*60*60 + (int(en[1]) - int(st[1]))*60 + (int(en[2]) - int(st[2]))
        return sec