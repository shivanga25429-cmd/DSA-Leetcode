
import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        freq = Counter(s)

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        ans = []
        prev_count = 0
        prev_char = ""

        while heap:
            count, char = heapq.heappop(heap)

            ans.append(char)

            # Put previously used character back
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            # Reduce current character frequency
            count += 1

            prev_count = count
            prev_char = char

        if len(ans) != len(s):
            return ""

        return "".join(ans)
