# 3668. Restore Finishing Order
# 5 mins to read and solve

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # convert friends into a set
        # traver order and see if element exists in set
        # if yes, add to ans array

        ans = []
        seen = set(friends)

        for value in order:
            if value in seen:
                ans.append(value)
        
        return ans