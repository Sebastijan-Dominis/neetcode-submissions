class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = { i : [] for i in range(1, n+1) }

        for trusting, trusted in trust:
            adj[trusting].append(trusted)
        
        suspicious = []
        for i in range(1, n+1):
            if not adj[i]:
                suspicious.append(i)
        
        for s in suspicious:
            for i in range(1, n+1):
                if i != s and s not in adj[i]:
                    break
            if i == n:
                return s
        
        return -1