# 206. Reverse Linked List
# 9 mins to read and solve

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Good but has redundant stuff 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use cur, prev and next ptr and traverse list and update accordingly
        
        # Not needed, prev will be returned as none
        if not head:
            return 
        
        # Not needed, prev will be returned as none
        if not head.next:
            return head

        cur = head
        prev = None

        # temp variable, can be declared inside loop
        nxt = None

        while cur:
            nxt = cur.next 

            # cur.next = prev handles both cases
            if cur == head:
                cur.next = None
            else:
                cur.next = prev

            prev = cur
            cur = nxt

        # no need to return as head, return as prev
        head = prev

        return head

# Best solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None

        while curr is not None:
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward

        return prev  

