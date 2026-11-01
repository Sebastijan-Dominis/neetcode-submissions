from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        expected = Counter(s1)

        l = 0
        actual = defaultdict(int)

        for r in range(len(s2)):
            actual[s2[r]] += 1
            
            while actual[s2[r]] > expected[s2[r]]:
                actual[s2[l]] -= 1
                l += 1

            if (r - l + 1) == len(s1):
                return True
        
        return False