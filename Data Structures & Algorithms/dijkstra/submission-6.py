class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for s, e, w in edges:
            adj[s].append((e, w))

        minHeap = [(0, src)]
        shortest = {}
        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v in shortest:
                continue
            
            shortest[v] = w
            for nei, w_nei in adj.get(v, ()):
                if nei not in shortest:
                    heapq.heappush(minHeap, (w+w_nei, nei))
            
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest