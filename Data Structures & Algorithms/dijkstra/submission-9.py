class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((d, w))
        
        shortest = {}

        heap = [(0, src)]

        while heap and len(shortest) < n:
            w, v = heapq.heappop(heap)
            if v in shortest:
                continue

            shortest[v] = w

            for nei, w_nei in adj.get(v, ()):
                if nei not in shortest:
                    heapq.heappush(heap, (w+w_nei, nei))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest