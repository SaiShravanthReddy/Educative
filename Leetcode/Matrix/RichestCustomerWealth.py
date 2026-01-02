# 1672. Richest Customer Wealth
# 3 mins to read and solve

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for name in accounts:
            ans = max(ans, sum(name))

        return ans

# Use of map()
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
        # return max(sum(person) for person in accounts)
