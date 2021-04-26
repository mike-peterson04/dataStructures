from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
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
