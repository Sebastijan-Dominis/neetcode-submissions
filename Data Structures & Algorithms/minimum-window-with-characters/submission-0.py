class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""

        countT = defaultdict(int)
        for c in t:
            countT[c] += 1

        l = 0
        window = defaultdict(int)
        have = 0
        need = len(countT.keys())
        res, resLen = [-1, -1], float("inf")

        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                currLen = r-l+1
                if currLen < resLen:
                    res = [l, r]
                    resLen = currLen

                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""