class Solution:
    # For each word, encode the length of the word followed by a delimiter character.
    # Because we know that the first part of each word is a number and the delimiter,
    # even if numbers or delimiters appear in the words, they will not be misinterpreted.
    # O(n) time.
    def encode(self, strs):
        # Using strick concatenation in a loop would be O(n*2).
        # Instead we can use a generator to make it O(n).
        # This uses f-strings.
        delim = "#"
        return  "".join([ f"{len(st)}{delim}{st}" for st in strs])

    def decode(self, str):
        delim = "#"
        res = []
        i = 0
        nrChars = ""
        while i < len(str):
            if str[i] == delim:
                wordLen = int(nrChars)
                res.append(str[i+1:i+wordLen+1])
                nrChars = ""
                i = i + wordLen
            else:
                nrChars += str[i]
            
            i += 1

        return res

sol = Solution()
print(sol.decode(sol.encode(["lint","code","love","you"])))