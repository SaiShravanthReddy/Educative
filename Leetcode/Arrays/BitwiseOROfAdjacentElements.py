# 3173. Bitwise OR of Adjacent Elements

class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        ans = []

        for index in range(1, len(nums)):
            ans.append(nums[index-1] | nums[index])

        return ans

class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [nums[i] | nums[i+1] for i in range(len(nums) - 1)]