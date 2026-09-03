class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        visit = set()

        # def dfs(e: int) -> None:
        #     visit.add(e)

        #     for nei in adj[e]:
        #         if nei not in visit:
        #             dfs(nei)

        # count = 0
        # for e in range(n):
        #     if e not in visit:
        #         count += 1
        #         dfs(e)
        # return count

        def bfs(q: deque) -> None:
            while q:
                e = q.popleft()
                visit.add(e)
                for nei in adj[e]:
                    if nei not in visit:
                        q.append(nei)
        
        count = 0
        for e in range(n):
            if e not in visit:
                count += 1
                bfs(deque([e]))
        return count
