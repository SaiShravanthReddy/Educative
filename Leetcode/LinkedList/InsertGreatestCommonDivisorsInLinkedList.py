# 2807. Insert Greatest Common Divisors in Linked List
# 6 mins to read and solve

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1%num2

        return num1

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse LL
        # use prev and cur
        # compute gcd of rev and cur, create node
        # prev.next = new node
        # new node.next = cur

        prev = head
        cur = head.next

        while cur:
            prev.next = ListNode(self.gcd(prev.val, cur.val), cur)

            prev = cur
            cur = cur.next
        
        return head