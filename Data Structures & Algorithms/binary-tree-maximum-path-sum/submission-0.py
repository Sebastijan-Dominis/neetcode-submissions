# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def searchSum(node):
            if not node:
                return 0
            
            leftCurr = searchSum(node.left)
            leftMax = max(0, leftCurr)
            rightCurr = searchSum(node.right)
            rightMax = max(0, rightCurr)

            self.res = max(self.res, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        searchSum(root)
        return self.res