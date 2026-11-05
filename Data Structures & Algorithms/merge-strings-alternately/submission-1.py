class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        res = ""

        while p < len(word1) and p < len(word2):
            res += word1[p]
            res += word2[p]
            p += 1
        
        while p < len(word1):
            res += word1[p]
            p += 1
        
        while p < len(word2):
            res += word2[p]
            p += 1
        
        return res