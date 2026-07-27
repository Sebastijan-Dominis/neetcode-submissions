class TreeNode:
    def __init__(self, key: int, val: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key=key, val=val)

        if self.root is None:
            self.root = node
            return
        
        curr = self.root
        while curr:
            if key > curr.key:
                if curr.right is None:
                    curr.right = node
                    return
                else:
                    curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    curr.left = node
                    return
                else:
                    curr = curr.left
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        if self.root is None:
            return -1
        
        curr = self.root
        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        if self.root is None:
            return -1
        
        curr = self.findMin(self.root)
        return curr.val

    def getMax(self) -> int:
        if self.root is None:
            return -1
        
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(key, self.root)

    def removeHelper(self, key: int, curr: "TreeNode | None") -> "TreeNode | None":
        if curr is None:
            return None
        
        if key > curr.key:
            curr.right = self.removeHelper(key, curr.right)
        elif key < curr.key:
            curr.left = self.removeHelper(key, curr.left)
        else:
            if curr.right is None:
                return curr.left
            elif curr.left is None:
                return curr.right
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(minNode.key, curr.right)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: "TreeNode | None", result: list[int]) -> None:
        if root is None:
            return
        
        self.inorderTraversal(root.left, result)
        result.append(root.key)
        self.inorderTraversal(root.right, result)





























