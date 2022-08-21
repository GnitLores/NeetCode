from typing import List
import heapq

class Solution:
    # Count the cards and detect the smallest and largest cards.
    # Iterate through possible cards starting from smallest.
    # E.g. if there are two card 1s, and the group size is three - subtract two from 1s, 2s, and 3s.
    # If any mismatch is detected, return False.
    # If it completes wihtout any issues, return True.
    # O(k * m) in priciple where k is number of possible cards and m is group size.
    # However, most of the iterations do very little so it is pretty efficient.
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not len(hand) % groupSize == 0:
            return False

        count = dict()
        for i, card in enumerate(hand):
            count[card] = count.get(card, 0) + 1
            if i == 0:
                minCard = card
                maxCard = card
            else:
                minCard = min(minCard, card)
                maxCard = max(maxCard, card)

        l = minCard
        r = maxCard
        while l <= r:
            c = count.get(l, 0)
            if c == 0:
                l += 1
                continue
            if c < 0: return False
            if l + groupSize - 1 > r: return False

            numberOfGroups = count[l]
            for dl in range(groupSize):
                count[l + dl] = count.get(l + dl, 0) - numberOfGroups
            l += 1
        return True

    # More efficient solution based on minheap.
    # Count cards as before.
    # Make minheap out of set of existing unique cards.
    # When a count reaches zero, check if it is the minimum card.
    # If not, there is a mismatch. We cannot have a count in the group reaching zero
    # while there is still another smaller minmum card.
    # The heap operations shoule be O(nlogn + m) time where n is the number of distincs cards,
    # and m is the total number of cards.

    def isNStraightHandMinHeap(self, hand: List[int], groupSize: int) -> bool:
        if not len(hand) % groupSize == 0:
            return False

        count = dict()
        for card in hand:
            count[card] = count.get(card, 0) + 1

        cards = list(count.keys())
        heapq.heapify(cards)

        while cards:
            minCard = cards[0]
            # For the smallest card, try to subtract one from each card in the group that should start.
            for dc in range(groupSize):
                c = minCard + dc # Next card count to subtract from
                if c not in count: # If the card doesn't exist - return false.
                    return False
                count[c] -= 1
                if count[c] == 0: # If there are no more of this card
                    if c != cards[0]: # And the card is different from the current minimum card
                        return False # Return false
                    heapq.heappop(cards) # Otherwise go to the next minmum card
        return True

        

        

sol = Solution()
print(sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(sol.isNStraightHand([1,2,3,4,5], 4))
print(sol.isNStraightHand([1,1,2,2,3,3], 3))
print(sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print("")
print(sol.isNStraightHandMinHeap([1,2,3,6,2,3,4,7,8], 3))
print(sol.isNStraightHandMinHeap([1,2,3,4,5], 4))
print(sol.isNStraightHandMinHeap([1,1,2,2,3,3], 3))
print(sol.isNStraightHandMinHeap([1,2,3,6,2,3,4,7,8], 3))