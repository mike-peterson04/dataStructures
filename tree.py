from node import TreeNode


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data, root=None):
        if self.root is None:
            if root is None:
                self.root = TreeNode(data)
                return
            else:
                self.root = root
        if root.data > data:
            if root.left is None:
                root.left = TreeNode(data)
            else:
                self.insert(data, root.left)
        else:
            if root.next is None:
                root.next = TreeNode(data)
            else:
                self.insert(data, root.next)
