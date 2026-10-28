class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)

        for card in sorted(freq):
            count = freq[card]
            if count == 0:
                continue
            for nxt in range(card, card + groupSize):
                if freq[nxt] < count:
                    return False
                freq[nxt] -= count
        return True
        