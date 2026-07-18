# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            nodes.append(curr.val)
            curr = curr.right

        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i-1]:
                return False
        return True