class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = defaultdict(int)


        for card in hand:
            freq[card] += 1

        for num in sorted(freq):
            
            while freq[num] > 0:
                for offset in range(groupSize):
                    if freq.get(num + offset, 0) == 0:
                        return False
                    freq[num + offset] -=1

        return True

                

                
