# 143. Reorder List
# 40 mins to read, solve and debug

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Index pointer to traverse 
        # cur and prev pointer to go to end of linked list
        # nxt = index.next
        # once cur is at end of list, cur.next = index.next
        # index.next = cur 
        # index = nxt
        # prev.next = None
        # while index.next != None or index.next.next != None 

        # not OR, its AND - biggest mistake - took 10 mins to debug 

        if not head:
            return

        index = head
        while index.next and index.next.next:
            nxt = index.next

            prev = index
            cur = index.next

            while cur.next:
                prev = cur
                cur = cur.next

            cur.next = index.next
            index.next = cur
            prev.next = None
            index = nxt
        