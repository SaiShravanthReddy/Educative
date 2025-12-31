# 3289. The Two Sneaky Numbers of Digitville
# 3 mins

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashmap = set()
        ans = []

        for val in nums:
            if val in hashmap:
                ans.append(val)
            else:
                hashmap.add(val)

        return ans