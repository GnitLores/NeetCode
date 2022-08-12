# Solution using trees.
# Store the first letter as nodes, and each subsequent letter as child nodes of child notes.
# Allows you to reuse the data and search efficiently.
# Mark nodes that are end of words.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

print("")
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))     # return True

print("")
trie = Trie()
trie.insert("a")
print(trie.search("a"))   # return True
print(trie.startsWith("a")) # return True

print("")
trie = Trie()
trie.insert("ab")
print(trie.search("a"))   # return False
print(trie.search("ab"))   # return True
print(trie.startsWith("a")) # return True
print(trie.startsWith("ab")) # return True


print("")