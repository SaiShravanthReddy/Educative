# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode

def get_middle_node(head):
    slow_pointer = head
    fast_pointer = head
    
    while fast_pointer != None and fast_pointer.next != None:
        print(slow_pointer.val, fast_pointer.val)
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    
    return slow_pointer