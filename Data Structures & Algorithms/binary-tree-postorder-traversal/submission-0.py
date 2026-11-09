# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorderHelper(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            postorderHelper(node.left)
            postorderHelper(node.right)
            res.append(node.val)
        
        postorderHelper(root)
        return res