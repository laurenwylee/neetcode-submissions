class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        freq = defaultdict(int)
        for x in hand:
            freq[x] += 1
        start = hand[0]
        while freq[start] > 0:
            for i in range(groupSize):
                if freq[start + i] <= 0:
                    return False
                freq[start + i] -= 1
            while freq[start] <= 0 and start <= hand[-1]:
                start += 1
        return True
        