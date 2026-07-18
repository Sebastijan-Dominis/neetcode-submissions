class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for b in s:
            if b in pairs:
                actual = brackets.pop() if brackets else None
                expected = pairs[b]
                if not actual == expected:
                    return False
            else:
                brackets.append(b)
        
        return not brackets