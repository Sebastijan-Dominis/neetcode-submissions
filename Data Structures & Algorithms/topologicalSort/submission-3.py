class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
        
        visited, visiting = set(), set()
        topSort = []

        def dfs(v: int) -> bool:
            if v in visited:
                return True
            
            if v in visiting:
                return False
            
            visiting.add(v)

            for nei in adj.get(v, ()):
                if not dfs(nei):
                    return False
            
            visiting.remove(v)
            visited.add(v)
            topSort.append(v)
            return True
        
        for v in range(n):
            if not dfs(v):
                return []
        
        topSort.reverse()
        return topSort