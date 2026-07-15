class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand) % groupSize != 0):
            return False

        freq = defaultdict(int)
        for h in hand:
            freq[h] += 1
        for n in hand:
            start = n
            while freq[start - 1] > 0:
                start -= 1
            while start <= n:
                while freq[start] > 0:
                    for i in range(groupSize):
                        if freq[start + i] <= 0:
                            return False
                        freq[start + i] -= 1
                start += 1
        return True
                    
        
