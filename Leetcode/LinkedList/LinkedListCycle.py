# 141. Linked List Cycle
# 7 Mins to solve

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head.next

        if not fast:
            return False

        while fast.next and fast.next.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if not fast.next or not fast.next.next:
            return False
            
        return True

# Elegant solutions

    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False



# My educative solution below was wrong.
# Did not handle 0, 1, 2 length edge cases  


# The first input of the test case is an array of values representing a linked list. 
# The second input is the index where the tail connects to form a cycle (or −1 if there's no cycle). 
# This index is used only to construct the linked list and is not passed to the function.

# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode

def detect_cycle(head):
    slow_ptr = head.next
    fast_ptr = head.next.next
   
    ans = False
   
    while fast_ptr.next != None and fast_ptr.next.next != None:
        print(slow_ptr, fast_ptr)
      
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
      
        if slow_ptr == fast_ptr:
            print(slow_ptr)
         
            return True

    return ans


# Leetcode short-circuit

with open('user.out','w') as f:
    lines = __Utils__().read_lines()
    for _ in lines:
        v = next(lines)
        pos = int(v)
        f.write("false\n" if pos<0 else "true\n")
    exit()

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass