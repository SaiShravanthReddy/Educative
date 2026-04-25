# BFS of Graph
# 27 mins to solve

# Space Complexity - O(v)
# Time Complexity - O(v + e)

# All test cases passed but, wrong implementation
from collections import deque

def bfs(self, adj):
    res = []
    seen = set()
    queue = deque()
    queue.append(0)
    seen.add(0)
    
    while len(queue) > 0:
        index = queue.popleft()
        
        if index not in seen:
            seen.add(index)
            res.append(index)
        
        for num in adj[index]:
            if num not in seen:
                seen.add(num)
                res.append(num) # dont add when discovered, only add when poped 
                queue.append(num)
    
    return res

# Better solution 
from collections import deque

def bfs(self, adj):
    res = []
    seen = set()
    queue = deque([0])
    seen.add(0)

    while queue:
        node = queue.popleft()
        res.append(node)   # ✅ Add when processing

        for nei in adj[node]:
            if nei not in seen:
                seen.add(nei)
                queue.append(nei)

    return res