class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if not letter in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if not letter in curr.children:
                return False
            curr = curr.children[letter]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if not letter in curr.children:
                return False
            curr = curr.children[letter]
        return True