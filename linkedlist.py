from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node

    def prepend_node(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def contains (self, data):
        if self.head is None:
            print("linked list is currently empty")
        else:
            temp = self.head
            while temp.data != data:
                if temp.next is not None:
                    temp = temp.next
                else:
                    return False
            return True
