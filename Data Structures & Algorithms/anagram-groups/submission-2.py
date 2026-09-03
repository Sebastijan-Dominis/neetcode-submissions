class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for anagram in strs:
            count = [0] * 26
            for letter in anagram:
                count[ord(letter) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(anagram)
        
        return list(anagrams.values())