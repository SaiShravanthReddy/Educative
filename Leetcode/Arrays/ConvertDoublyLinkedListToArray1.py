# 3263. Convert Doubly Linked List to Array 1
# Easy
# 2 mins

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        cur = root
        ans = []

        while cur:
            ans.append(cur.val)
            cur = cur.next
        
        return ans