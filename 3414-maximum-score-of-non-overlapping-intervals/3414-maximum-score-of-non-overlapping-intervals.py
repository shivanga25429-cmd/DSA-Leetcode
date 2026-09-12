class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rs = [intervals[i][1] for i in order]

        def bisect_left(arr, x):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def insort(arr, x):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            arr.insert(lo, x)

        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(1, n + 1):
            orig = order[i - 1]
            l, r, w = intervals[orig]
            p = bisect_left(rs, l)

            dp[i][0] = (0, ())
            for k in range(1, 5):
                skip_score, skip_list = dp[i - 1][k]

                take_score = dp[p][k - 1][0] + w
                take_list = list(dp[p][k - 1][1])
                insort(take_list, orig)
                take_list = tuple(take_list)

                if take_score > skip_score or (take_score == skip_score and take_list < skip_list):
                    dp[i][k] = (take_score, take_list)
                else:
                    dp[i][k] = (skip_score, skip_list)

        return list(dp[n][4][1])
