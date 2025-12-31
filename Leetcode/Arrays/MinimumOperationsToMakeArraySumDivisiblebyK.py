# 3512. Minimum Operations to Make Array Sum Divisible by K
# Easy
# 2 mins

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # add total of the array and modulo divide by k

        count = 0
        for val in nums:
            count += val
        
        return count%k