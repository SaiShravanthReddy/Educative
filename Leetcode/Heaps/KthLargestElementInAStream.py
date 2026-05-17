# 703. Kth Largest Element in a Stream
# Easy question
# 28 mins to solve

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(nums) # I used nums instead of self.nums

        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        heapq.heappushpop(self.nums, val)

        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# took 15 mins to solve
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.list = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.list, val)

        while len(self.list) > self.size:
            heapq.heappop(self.list)

        return self.list[0]
