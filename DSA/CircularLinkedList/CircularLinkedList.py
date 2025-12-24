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
        
    def remove_node(self, key):
        # traverse ll
        # use prev and cur
        # make changes
        if not self.head:
            return

        cur = self.head

        if cur.data == key and cur == self.head:
            # single node case
            if cur.next == self.head:
                self.head = None
                return

            # traverse till the end and assign to prev
            prev = cur
            while prev.next != self.head:
                prev = prev.next
            
            prev.next = self.head.next
            # cur = None -> No use
            self.head = self.head.next

            return
        
        prev = cur
        cur = cur.next
        
        while cur != self.head:
            if cur.data == key:
                prev.next = cur.next 
                # cur = None -> No use
                return
            
            prev = cur
            cur = cur.next

    def len(self):
        if not self.head:
            return 0
        
        cur = self.head.next
        count = 1

        while cur != self.head:
            cur = cur.next
            count += 1
        
        return count

    def split_list(self):
        len_cll = self.len()
        if len_cll == 0:
            print("Empty circular linked list")
            return
        
        if len_cll == 1:
            print("Circular Linked List of length 1, cannot split")
            return

        split_index = len_cll//2
        cur = self.head

        while split_index > 0:
            prev = cur
            cur = cur.next
            split_index -= 1

        prev.next = self.head
        
        new_cll = CircularLinkedList()
        new_cll.head = cur

        while cur.next != self.head:
            cur = cur.next

        cur.next = new_cll.head

        self.print_list()
        new_cll.print_list()
