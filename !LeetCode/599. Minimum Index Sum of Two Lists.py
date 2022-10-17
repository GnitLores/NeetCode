from typing import List


class Solution:
    # This can be solved in linear time by mapping the words of one list to their index
    # positions with a dictionary and then run through the second list, finding the sum
    # of the index position in the second list and the mapped position in the first list
    # if the word actually was found in the first list.
    # We just track the smallest sum and assemble the output list.
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minSum = float("Inf")
        res = []
        hashmap = dict()
        
        for i, w in enumerate(list1):
            hashmap[w] = i

        for i, w in enumerate(list2):
            if w not in hashmap: continue
            iSum = hashmap[w] + i
            if iSum < minSum:
                res = [w]
                minSum = iSum
            elif iSum == minSum:
                res.append(w)
        return res

sol = Solution()
print(sol.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(sol.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
print(sol.findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))
print(sol.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]))