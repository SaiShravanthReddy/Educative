class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # null pointer
        # traverse and append
        new_node = Node(data)

        if not self.head:
            self.head = new_node

            return
        
        cur = self.head
        
        while cur.next:
            cur = cur.next
        
        cur.next = new_node
        new_node.prev = cur

    def print_list(self):
        cur = self.head
        if not cur:
            return

        while cur:
            print(cur.data)
            cur = cur.next

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node

            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        
    def add_after_node(self, key, data):
        # Took 5 mins
            # check if dll is none or not
            # traverse to the key 
            # point new_node to next node 
            # and current node as prev
            # then the other two

        # Took 5 mins - edge cases
            # if append on end node

        if not self.head:
            print("Empty linked list")
            return 

        cur = self.head

        while cur and cur.data != key:
            cur = cur.next

        if cur == None:
            print("Key not found in the Linked List")
            return 

        new_node = Node(data)

        new_node.next = cur.next
        new_node.prev = cur

        # cur.next = new_node
        # because of the edge case handle, - Change in logic
        # this line should have been below the condition

        # for adding at the end of linked list
        if cur.next:
            cur.next.prev = new_node
            
        cur.next = new_node


    def add_before_node(self, key, data):
        # check if dll is None or not
        # traverse till the key
        # first do new node pointers
        # then do before and after node pointers
        # handle prepend case

        if not self.head:
            print("Empty linked list")

        cur = self.head

        while cur and cur.data != key:
            cur = cur.next

        if cur == None:
            print("Key not found in the Linked List")
            return     

        new_node = Node(data)

        new_node.next = cur
        new_node.prev = cur.prev

        if cur.prev:
            cur.prev.next = new_node
        
        cur.prev = new_node
    


dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()