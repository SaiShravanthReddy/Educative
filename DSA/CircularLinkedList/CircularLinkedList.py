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
        else:
            cur = self.head

            while cur.next != self.head:
                cur = cur.next 
            
            new_node.next = self.head
            cur.next = new_node
        
        self.head = new_node
    


