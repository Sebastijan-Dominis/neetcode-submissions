class Node:
    def __init__(self, total: int, l: int, r: int, left: "Node | None" = None, right: "Node | None" = None):
        self.sum = total
        self.l = l
        self.r = r
        self.left = left
        self.right = right

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums: list[int], l: int, r: int) -> Node:
        if l == r:
            return Node(nums[l], l, r)
        
        curr = Node(0, l, r)
        m = (l+r) >> 1

        curr.left = self.build(nums, l, m)
        curr.right = self.build(nums, m+1, r)
        curr.sum = curr.left.sum + curr.right.sum
        return curr

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, curr: Node, index: int, val: int) -> Node:
        if curr.l == curr.r:
            curr.sum = val
            return curr
        
        m = (curr.l+curr.r) >> 1

        if index > m:
            curr.right = self.update_helper(curr.right, index, val)
        else:
            curr.left = self.update_helper(curr.left, index, val)
        curr.sum = curr.left.sum + curr.right.sum
        return curr

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, curr: Node, l: int, r: int) -> int:
        if curr.l >= l and curr.r <= r:
            return curr.sum
        
        if curr.l > r or curr.r < l:
            return 0
        
        return self.query_helper(curr.left, l, r) + self.query_helper(curr.right, l, r)



























