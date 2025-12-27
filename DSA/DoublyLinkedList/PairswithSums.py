def pairs_with_sum(self, sum_val):
    # 10 mins to solve
    # But ans is not in order to what Educative expects
    # So return reverse list/array

    # create a hashmap to keep track of value
    # traverse the dll
    # check if diff exisits in hashmap
    # if it exists add it to ans array
    
    ans = []
    seen = set()
    
    cur = self.head
    
    while cur:
        diff = sum_val - cur.data
        
        if diff in seen:
            ans.append("(" +  str(diff) + "," + str(cur.data) + ")")
        else:
            seen.add(cur.data)
        
        cur = cur.next
    
    return ans[::-1]

# Educative ans - Two pointers, O(n^2)
def pairs_with_sum(self, sum_val):
  pairs = list()
  p = self.head 
  q = None 
  while p:
    q = p.next
    while q:
      if p.data + q.data == sum_val:
          pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
      q = q.next
    p = p.next
  return pairs