class Solution:
    # The main difficulty is dealing with the fact that the name can have
    # repeated characters, so when encountering repeated characters in the
    # typed input we need to take into account that they may sometimes be valid
    # and sometimes invalid input.
    # This solution works by comparing char by char, and checking if it is the first
    # of a a repeated char in the name.
    # If it is not, we always skip all the next occureences of this char in the input.
    # However, if it is, we only increment that index in the typed input by one and wait
    # for the next char to see if we can skip past the rest.
    # If we ever encounter the wrong char or if the index in the typed input ever goes out
    # of bounds, the input cannot be valid.
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed): return False

        typedIdx = 0
        for i, c in enumerate(name):
            if typedIdx >= len(typed): return False
            if c != typed[typedIdx]: return False

            if i < len(name) - 1 and c == name[i + 1]:
                typedIdx += 1
            else:
                while typedIdx < len(typed) and c == typed[typedIdx]:
                    typedIdx += 1

        return typedIdx == len(typed)
    
sol = Solution()
print(sol.isLongPressedName(name = "alexd", typed = "ale"))
print(sol.isLongPressedName(name = "alex", typed = "aaleexa"))
print(sol.isLongPressedName(name = "alex", typed = "aaleex"))
print(sol.isLongPressedName(name = "saeed", typed = "ssaaedd"))