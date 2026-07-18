class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        i, j = 0, 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length
            dec.append(s[i:j])

            i = j
        
        return dec