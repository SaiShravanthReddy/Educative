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

    # def print_list(self):
    #     cur = self.head
    #     if not cur:
    #         return

    #     while cur:
    #         print(cur.data)
    #         cur = cur.next

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
        # Took 7 mins to solve
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
    
    def delete(self, key):
        # 7 mins to solve
        # 8 mins to debug edge cases

        # no linked list
        # single linked list
        # start, end, middle

        # 0 len list
        if not self.head:
            print("Empty linked list")
            return
        
        # 1 len list
        if self.head.data == key and not self.head.next:
            self.head = None
            return

        # between
        cur = self.head

        while cur and cur.data != key:
            cur = cur.next
        
        if cur == None:
            print("Key not found in the Linked List")
            return 

        if cur.prev:
            cur.prev.next = cur.next
        
        if cur.next:
            cur.next.prev = cur.prev
        
        if not cur.prev:
            self.head = cur.next

    def reverse(self):
        # 7 mins to write code
        # 8 mins to debug

        # traverse and exchane prev and next
        # handle head and tail
        # set tail as head

        if not self.head:
            print("Empty linked list")
            return
        
        cur = self.head
        prev = None
        
        while cur:
            cur.prev, cur.next = cur.next, cur.prev

            prev = cur
            cur = cur.prev
        
        self.head = prev
        
    def remove_duplicates(self):
        cur = self.head 
        seen = set()
        
        while cur:
            if cur.data not in seen:
                seen.add(cur.data)
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt

    def pairs_with_sum(self, sum_val):
        # 10 mins to solve
        # But ans is not in order to what Educative expects

        # create a hashmap to keep track of value
        # traverse the dll
        # check if diff exisits in hashmap
        # if it exists add it to ans array
        
        ans = []
        seen = set()
        
        cur = self.head
        
        while cur:
            diff = sum_val - cur.data
            
            if diff in seen:
                ans.append("(" +  str(diff) + "," + str(cur.data) + ")")
            else:
                seen.add(cur.data)
            
            cur = cur.next
        
        return ans


dllist = DoublyLinkedList()
# dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

dllist.print_list()

print(pairs_with_sum(dllist, 5))