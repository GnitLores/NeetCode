import collections


class Solution:
    # Solution using character counts.
    # If the counts are different, you can't swap chars in the strings counts equal
    # because swapping does not change the count.
    # If the strings are identical, you can swap two identical characters in the string
    # to get the goal, so check if there are any duplicate characters to swap.
    # If the strings  are not identical, you can get the goal string if the strings
    # differ by exactly two characters by swapping those characters.
    # O(n) time.
    def buddyStrings(self, s: str, goal: str) -> bool:
        count1, count2 = collections.Counter(s), collections.Counter(goal)
        if count1 != count2 : return False
        if s == goal and count1.most_common()[0][1] > 1: return True
        if sum([x != y for x, y in zip(s, goal)]) == 2: return True
        return False

sol = Solution()
print(sol.buddyStrings(s = "ab", goal = "ba"))
print(sol.buddyStrings(s = "ab", goal = "ab"))
print(sol.buddyStrings(s = "aa", goal = "aa"))
print(sol.buddyStrings(s = "aa", goal = "ac"))