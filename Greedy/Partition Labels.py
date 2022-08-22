from typing import List


class Solution:
    # Observation - if you count all letters in string and start iterating, if you subtract
    # the count of letters in the partition from the total count, the moment that ALL letters
    # in the partition have a count of zero, this is a valid partition.
    # This algorithm uses a set to check for letters in partition and a
    # total letter count in order to avoid having to loop within the loop.
    # O(n) time.
    def partitionLabels(self, s: str) -> List[int]:
        count = dict()
        for c in s:
            count[c] = count.get(c, 0) + 1

        res = []
        partLetters = set() # Unique set of letters already added to partitions.
        partCount = 0 # Number of times all letters in partition occur right of partition.
        partLength = 0 # Length of partition
        for c in s:
            partLength += 1
            partCount -= 1

            if c not in partLetters: # Add new letter to partition.
                partLetters.add(c)
                partCount += count[c]

            if partCount == 0: # If all letters in partition occur no more - valid partition.
                res.append(partLength)
                partLength = 0

        return res

    # Even simpler and more efficient solution.
    # Instead of counting letters we just map the last occurrence of each letter.
    # Iterate through, updating what the minimal endpoint of the partition must be
    # by checking the current letter in the hashmap and updating the minimal endpoint
    # if we reach a letter with a later occurrence.
    # If we ever reach the minimal endpoint, this is a valid partition.
    # O(n) time as well.
    def partitionLabelsLastLetter(self, s: str) -> List[int]:
        last = dict()
        for i, c in enumerate(s):
            last[c] = i
        
        res =  []
        minEnd = 0
        partLength = 0
        for i, c in enumerate(s):
            partLength += 1
            minEnd = max(minEnd, last[c])
            if i == minEnd:
                res.append(partLength)
                partLength = 0

        return res



sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels("eccbbbbdec"))
print("")
print(sol.partitionLabelsLastLetter("ababcbacadefegdehijhklij"))
print(sol.partitionLabelsLastLetter("eccbbbbdec"))