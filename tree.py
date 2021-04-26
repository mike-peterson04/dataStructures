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
        elif root.data < data:
            if root.next is None:
                root.next = TreeNode(data)
            else:
                self.insert(data, root.next)
        else:
            print("value already exists")

    def search(self, data):
        if self.root is None:
            print("search tree is currently empty")
        else:
            temp = self.root
            while temp.data != data:
                if temp.data < data:
                    if temp.next is not None:
                        temp = temp.next
                    else:
                        return False
                else:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        return False
            return True

    def in_order(self, root=None):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data)
        self.in_order(root.next)

    def pre_order(self, root=None):
        if root is None:
            return
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.next)
