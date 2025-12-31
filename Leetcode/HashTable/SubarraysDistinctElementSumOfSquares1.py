# 2913. Subarrays Distinct Element Sum of Squares 1
# 14 mins to read and solve
# O(n^2) solution, there is no better solution afaik

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # count += len for subarry size 1
        # construct 2 len sbarrays and so on till full len
        # convert each size array to set and count elements in set and square them and add them

        ans = len(nums)

        size = 1

        while size < len(nums):
            first = 0
            second = first + size

            while second < len(nums):
                ans += (len(set(nums[first:second+1])))**2

                first += 1
                second += 1

            size += 1

        return ans