class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class TreeNode(Node):

    def __init__(self, data):
        super().__init__(data)
        self.left = None
