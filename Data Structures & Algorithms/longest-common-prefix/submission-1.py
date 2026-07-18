class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = list(strs[0])
        for word in strs:
            letters = list(word)
            chars = chars[0:min(len(chars), len(letters))]
            for i in range(len(chars)):
                if chars[i] != letters[i]:
                    chars = chars[0:i]
                    break
        return ''.join(chars)