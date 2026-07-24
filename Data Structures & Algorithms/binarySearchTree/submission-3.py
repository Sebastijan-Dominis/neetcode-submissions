class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        curr = self.root
        new_node = TreeNode(key=key, val=val)
        if curr is None:
            self.root = new_node
            return
        
        while True:
            if key > curr.key:
                if curr.right is None:
                    curr.right = new_node
                    return
                curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    curr.left = new_node
                    return
                curr = curr.left
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
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
        curr = self.root
        if curr is None:
            return -1
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        curr = self.root
        if curr is None:
            return -1
        while curr.right:
            curr = curr.right
        return curr.val

    def findMin(self, curr: TreeNode) -> TreeNode:
        while curr.left:
            curr = curr.left
        return curr

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr is None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.right is None:
                return curr.left
            elif curr.left is None:
                return curr.right
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
    
    def inorderTraversal(self, root: TreeNode, result: list[int]) -> None:
        if root is None:
            return
        
        self.inorderTraversal(root.left, result)
        result.append(root.key)
        self.inorderTraversal(root.right, result)