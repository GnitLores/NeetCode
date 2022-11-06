class Solution:
    # Use set of lower and upper case vowels to check for first letter being vowel.
    # Split sentence into words, and for each word, add it to a list and move first letter to back if not vowel.
    # Add suffixes to list and join into new word.
    # Join all new words to new sentence.
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        sentence = sentence.split()
        for i, w in enumerate(sentence):
            nw = [w] if w[0] in vowels else [w[1:], w[0]]
            nw.append("ma")
            nw.append("a" * (i + 1))
            sentence[i] = "".join(nw)
        return " ".join(sentence)

sol = Solution()
print(sol.toGoatLatin(sentence = "I speak Goat Latin"))
print(sol.toGoatLatin(sentence = "The quick brown fox jumped over the lazy dog"))