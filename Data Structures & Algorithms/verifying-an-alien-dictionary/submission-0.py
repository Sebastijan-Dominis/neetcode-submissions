class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_ordering = { letter: position for position, letter in enumerate(order) }

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            
            for j in range(max(len(word1), len(word2))):
                if j >= len(word2):
                    return False

                if j >= len(word1):
                    break

                a, b = letter_ordering[word1[j]], letter_ordering[word2[j]]
                if a != b:
                    if a > b:
                        return False
                    break
        
        return True