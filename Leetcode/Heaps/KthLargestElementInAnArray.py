# 215. Kth Largest Element in an Array
# 4 min 34 sec
# Medium

# I have solved this under ChatGPT folder too

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

# Space Complexity - O(n log k)
# Time Complexity - O(k)


import heapq

class Solution:
    def findKthLargest(self, nums, k):

        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:

            if num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]