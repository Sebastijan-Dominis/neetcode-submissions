class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if not letter in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    for child in root.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
            return root.endOfWord
        
        return dfs(0, self.root)