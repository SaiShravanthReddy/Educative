class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            new_node.next = new_node
            self.head = new_node

            return

        cur = self.head

        while cur.next != self.head:
            cur = cur.next 
            
        new_node.next = self.head
        cur.next = new_node
        self.head = new_node
    
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            new_node.next = new_node
            self.head = new_node
            
            return 
        
        cur = self.head

        while cur.next != self.head:
            cur = cur.next
        
        new_node.next = self.head
        cur.next = new_node

    def print_list(self):
        if not self.head:
            return None
        
        cur = self.head

        while True:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
        