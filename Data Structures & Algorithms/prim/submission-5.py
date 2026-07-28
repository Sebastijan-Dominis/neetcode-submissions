class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2, w in edges:
            adj[v1].append((v2, w))
            adj[v2].append((v1, w))
        
        mst = 0
        visit = set()
        heap = [(0, 0)]

        while heap and len(visit) < n:
            w, v = heapq.heappop(heap)
            if v in visit:
                continue
            
            visit.add(v)
            mst += w

            for nei, w_nei in adj.get(v, ()):
                if nei not in visit:
                    heapq.heappush(heap, (w_nei, nei))
        
        return mst if len(visit) == n else -1