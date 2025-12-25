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