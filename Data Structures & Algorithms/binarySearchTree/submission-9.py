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
        new_node = TreeNode(key, val)
        if self.root is None:
            self.root = new_node
        
        curr = self.root
        while curr:
            if key > curr.key:
                if curr.right is None:
                    curr.right = new_node
                    return
                else:
                    curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    curr.left = new_node
                    return
                else:
                    curr = curr.left
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if curr.key == key:
                return curr.val
            elif key > curr.key:
                curr = curr.right
            else:
                curr = curr.left
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

    def findMin(self, node: "TreeNode"):
        while node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.remove_helper(self.root, key)
    
    def remove_helper(self, curr: "TreeNode | None", key: int) -> "TreeNode | None":
        if curr is None:
            return None
        
        if key > curr.key:
            curr.right = self.remove_helper(curr.right, key)
        elif key < curr.key:
            curr.left = self.remove_helper(curr.left, key)
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.remove_helper(curr.right, minNode.key)
        
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, curr: "TreeNode | None", result: list[int]):
        if curr is None:
            return
        
        self.inorderTraversal(curr.left, result)
        result.append(curr.key)
        self.inorderTraversal(curr.right, result)