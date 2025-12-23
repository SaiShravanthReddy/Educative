class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
  
    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
  
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_by_value(self, value):
        cur_node = self.head

        if cur_node and cur_node.data == value:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev_node = None

        while cur_node and cur_node.data != value:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if cur_node and pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        
        index = 0
        prev_node = None
        while cur_node and index < pos:
            prev_node = cur_node
            cur_node = cur_node.next
            index += 1

        if cur_node is None:
            return 

        prev_node.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            cur_node = cur_node.next
            count +=1

        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        
        return 1 + self.len_recursive(node.next)
        
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev1 = None
        cur1 = self.head

        while cur1 and cur1.data != key_1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head

        while cur2 and cur2.data != key_2:
            prev2 = cur2
            cur2 = cur2.next
        
        if not cur1 or not cur2:
            return
        
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        
        cur1.next, cur2.next = cur2.next, cur1.next


    def reverse_iterative(self):
        prev = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(prev, cur):
            if not cur:
                return prev
            
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

            return _reverse_recursive(prev, cur)
        
        self.head = _reverse_recursive(prev=None,cur=self.head)

    # def merge_sorted(self, llist):
    #     ll1 = self.head
    #     ll2 = llist.head

    #     if ll1.data < ll2.data:

    def remove_duplicates(self):
        # traverse linked list
        # keep track of values using has table
        # remove duplicated when you find them

        cur = self.head

        if not cur:
            return None
        
        prev = None

        hashmap = {}

        while cur:
            if hashmap.get(cur.data):
                prev.next = cur.next
                cur = None
                
            else:
                hashmap[cur.data] = 1
                prev = cur
            
            cur = prev.next







        
llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("A")
llist.append("D")

print("Original Linked List")
llist.print_list()

# llist.prepend("D")

# llist.insert_after_node(llist.head.next, "F")

# llist.delete_by_value("F")

# print(llist.len_recursive(llist.head))

# llist.swap_nodes("A","D")

# llist.reverse_iterative()

# llist.reverse_recursive()

llist.remove_duplicates()

print("Linked List After Operation")
llist.print_list()



# ll1 = LinkedList()
# ll1.append(1)
# ll1.append(5)
# ll1.append(6)
# ll1.append(8)

# ll2 = LinkedList()
# ll2.append(2)
# ll2.append(3)
# ll2.append(4)
# ll2.append(7)

# ll1.merge_sorted(ll1.head, ll2)
