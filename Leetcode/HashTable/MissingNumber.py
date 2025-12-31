# 268. Missing Number
# 4 mins to solve

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # traverse the array, set value to 1
        # traverse hashmap, if number not in list return number

        seen = set(nums)

        for index in range(0, len(nums)+1):
            if index not in seen:
                return index