class Node:
    def __init__(self, total: int, L: int, R: int, left: "Node | None" = None, right: "Node | None" = None):
        self.sum = total
        self.L = L
        self.R = R
        self.left = left
        self.right = right

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums: list[int], L, R):
        if L == R:
            return Node(nums[L], L, R)
        
        M = (L+R) >> 1
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root: Node, index:int, val: int) -> None:
        if root.L == root.R:
            root.sum = val
            return
        
        M = (root.L+root.R) >> 1
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, root: Node, L: int, R: int) -> int:
        if root is None or (root.L >= L and root.R <= R):
            return root.sum
        
        if root.R < L or root.L > R:
            return 0

        return self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R)


