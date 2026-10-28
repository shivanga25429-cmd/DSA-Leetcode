class Solution(object):
    def frequencySort(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        n = len(s)
        buckets = [[] for _ in range(n + 1)]
        for ch, f in freq.items():
            buckets[f].append(ch)

        res = []
        for f in range(n, 0, -1):
            for ch in buckets[f]:
                res.append(ch * f)

        return "".join(res)
        
