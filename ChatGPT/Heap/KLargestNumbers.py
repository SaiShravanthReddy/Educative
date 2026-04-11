# You are given an array of integers and a number k.
# Return the k largest elements in the array.

# time complexity O(n log n)
# space complexity O(n)

import heapq

def k_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)

    return [-1*heapq.heappop(heap) for _ in range(k)]

nums = [3,2,1,5,6,4]
k = 2
print(k_largest(nums, k))

# time complexity O(n log k)
# space complexity O(k)

def k_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop()
        
    return heap
