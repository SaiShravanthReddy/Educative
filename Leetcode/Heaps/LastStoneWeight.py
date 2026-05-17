# 1046. Last Stone Weight
# 7 min 44 secs
# Easy

# create a max heap 
# get two largest and subtract those
# push it back to heap
# repeat 

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) != 1:
            stone1 = -1 * heapq.heappop(heap)
            stone2 = -1 * heapq.heappop(heap)

            heapq.heappush(heap, -1 * (stone1 - stone2)) # I am pushing 0 also into the heap
            # Surprisingly not caring of edge condition works in my favour.
            # I dont have to write - return -stones[0] if stones else 0 like ChatGPT
        
        return -1 * heap[0]
    
# Space Complexity - O(n) 
# Time Complexity - O(n log n)

# ChatGPT Ans
import heapq

class Solution:
    def lastStoneWeight(self, stones):

        # Convert to max heap using negatives
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            y = -heapq.heappop(stones)  # largest
            x = -heapq.heappop(stones)  # second largest

            if y != x:
                heapq.heappush(stones, -(y - x))

        return -stones[0] if stones else 0