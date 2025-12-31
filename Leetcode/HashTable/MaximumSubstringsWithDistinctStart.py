# 3760. Maximum Substrings With Distinct Start
# Medium
# 3 mins to read and solve

class Solution:
    def maxDistinct(self, s: str) -> int:
        # traverse the str
        # add chars to set
        # return len of set

        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
    
        return len(seen)

class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))