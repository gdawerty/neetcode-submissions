class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len (hand) % groupSize > 0:
            return False

        hand = sorted(hand)

        counts = defaultdict(int)

        for num in hand:
            counts[num] +=1

        for num in hand:
            if counts[num] > 0:
                for i in range(groupSize):
                    if num + i not in counts:
                        return False

                    counts[num + i] -=1

                    if counts[num + i] == 0:
                        del counts[num + i]

        return True
