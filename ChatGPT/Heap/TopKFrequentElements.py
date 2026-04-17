# Input
# nums = [1,1,1,2,2,3]
# k = 2

# Output
# [1,2]

# My solution

# Build freq map
# Iterate through the map
# Push (freq, num)
# Get result

import heapq

def topKFrequent(nums, k):
    heap = []
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    for key, value in freq.items():
        heapq.heappush(heap, (value, key))

        if len(heap) > k:
            heapq.heappop(heap)

    ans = []
    for _,j in heap:
        ans.append(j)

    return(ans)

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))

# Time Complexity - n + m log k, n - total, m - unique numbers
# Space Complexity - m + k

# Cleaner code
import heapq

def topKFrequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    heap = []
    for num, count in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (count, num))
        else:
            heapq.heappushpop(heap, (count, num))

    return [num for count, num in heap]

# There is a better soltuion to solve this - Bucket sort 