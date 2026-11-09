# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)

        if not root:
            return node

        prev = root
        curr = root

        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        if val > prev.val:
            prev.right = node
        else:
            prev.left = node
        
        return root