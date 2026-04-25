# DFS of Graph

class Solution:
    # traverse adj by index
    # add index to seen
    # add vetrices visited to seen 
    # if vertex already in seen, skip and continue iterating
    # iterator + dfs recursion
    
    def printDFS(self, seen, index, adj):    
        for num in adj[index]:
            if num not in seen: 
                seen.add(num)
                print(num, end=" ")
                
                self.printDFS(seen, num, adj)
   
    def dfs(self, adj):
        seen = set()
       
        for index in range(len(adj)):
            if index not in seen:
                seen.add(index)
                print(index, end=" ")
                
                self.printDFS(seen ,index, adj)

#Better solution

# Space Complexity - O(vertices)
# Time Complexity - O(vertices + edges)

class Solution:
    def dfs(self, adj):
        seen = set()
        result = []

        def dfs_util(node):
            if node in seen:
                return
            
            seen.add(node)
            result.append(node)

            for nei in adj[node]:
                dfs_util(nei)

        for node in range(len(adj)):
            if node not in seen:
                dfs_util(node)

        return result