class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
                
        hand.sort()
        count = Counter(hand)

        for num in hand:

            if count[num]:

                for key in range(num, num + groupSize):
                    if count[key] == 0:
                        return False
                    count[key] -= 1
        
        return True
