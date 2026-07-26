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
    
    def build(self, nums: list[int], L: int, R: int) -> Node:
        if L == R:
            return Node(nums[L], L, R)
        
        root = Node(0, L, R)
        M = (L+R) >> 1
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, curr: Node, index: int, val: int) -> None:
        if curr.L == curr.R:
            curr.sum = val
            return
        
        M = (curr.L+curr.R) >> 1
        if index > M:
            self.update_helper(curr.right, index, val)
        else:
            self.update_helper(curr.left, index, val)
        curr.sum = curr.left.sum + curr.right.sum
    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, curr: Node, L: int, R: int) -> int:
        if curr.L >= L and curr.R <= R:
            return curr.sum
        
        if curr.L > R or curr.R < L:
            return 0

        return self.query_helper(curr.left, L, R) + self.query_helper(curr.right, L, R)