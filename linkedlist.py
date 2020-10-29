class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    

    def append(self,data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
