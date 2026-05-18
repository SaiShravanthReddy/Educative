# 973. K Closest Points to Origin
# 8 mins 
# Medium

# I have solved this under ChatGPT folder too

# traverse points and compute distance
# use distance as priority key and push to min heap
# pop k closest points and append to ans and return
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            heapq.heappush(heap, (point[0]**2 + point[1]**2, point))
        
        ans = []
        while k > 0:
            val = heapq.heappop(heap)
            ans.append(val[1])

            k-=1

        return ans
    
# Space Complexity - O(n)
# Time Complexity - O(n log n)

#ChatGPT Sol, better

# Space Complexity - O(k)
# Time Complexity - O(n log k)

import heapq

class Solution:
    def kClosest(self, points, k):

        heap = []

        for x, y in points:

            dist = -(x*x + y*y)

            heapq.heappush(heap, (dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for dist, point in heap]