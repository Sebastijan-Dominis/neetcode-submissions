class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n-1:
            return False
        
        adj = [[] for _ in range(n)]
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visit = set()

        def dfs_valid_tree(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if not nei == prev:
                    if not dfs_valid_tree(nei, node):
                        return False
            
            return True
        
        return dfs_valid_tree(0, -1) and len(visit) == n