"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}

        def dfs(node):
            if not node:
                return None

            if node.val in nodes:
                return nodes[node.val]

            copy = Node(val=node.val)
            nodes[node.val] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node)