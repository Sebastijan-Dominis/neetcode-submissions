class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        components = 0
        included = set()

        def dfs(e: int) -> None:
            included.add(e)

            for nei in adj.get(e, ()):
                if nei not in included:
                    dfs(nei)
        
        for e in range(n):
            if e not in included:
                components += 1
                dfs(e)
        
        return components