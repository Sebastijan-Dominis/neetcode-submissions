# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        pre_idx = 0

        def dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None

            nonlocal pre_idx

            node_val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(val=node_val)

            mid = indices[node_val]

            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)

            return node
        
        return dfs(0, len(preorder)-1)