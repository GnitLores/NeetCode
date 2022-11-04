class Solution:
    # Use ascii value to index into list of morse characters.
    # Join morse characters into morse word and add to set of unique morse words.
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        wordSet = set()
        for w in words:
            morseWord = "".join([morse[ord(c) - ord("a")] for c in w])
            wordSet.add(morseWord)

        return len(wordSet)

sol = Solution()
print(sol.uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))
print(sol.uniqueMorseRepresentations(words = ["a"]))