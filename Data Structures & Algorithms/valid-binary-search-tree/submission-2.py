# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.inorderTraversal(root, values)

        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False
            
        return True
    
    def inorderTraversal(self, node: Optional[TreeNode], values: list[int]) -> None:
        if not node:
            return
        
        self.inorderTraversal(node.left, values)
        values.append(node.val)
        self.inorderTraversal(node.right, values)