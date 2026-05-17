# 1791. Find Center of Star Graph
# Easy
# 11 min to solve

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        set1 = set(edges[0])
        set2 = set(edges[1])

        value = set1.intersection(set2)

        for x in value:
            return x

# Other solution
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a,b = edges[0]
        c,d = edges[1]
        if a == c or a == d:
            return a
        else:
            return b
        
