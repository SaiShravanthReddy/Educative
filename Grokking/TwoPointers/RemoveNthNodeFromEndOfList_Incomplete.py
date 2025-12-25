# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode

def remove_nth_last_node(head, n):
    currentNode = head
    length = 1
    
    while currentNode.next != None:
        currentNode = currentNode.next
        length += 1
    
    print("length", length)
    
    index = length - n
    print("index", index)
    
    currentNode = head
    
    while index >= 0:
        # currentNode = currentNode.next
        
        if index == 0:
            currentNode.next = currentNode.next.next
        
        index -= 1
            
        print("index",index)
        

    return head