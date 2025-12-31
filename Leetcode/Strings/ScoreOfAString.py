# 3110. Score of a String
# 2 mins to solve

class Solution:
    def scoreOfString(self, s: str) -> int:
        # traverse the string
        # use ord
        # keep track of count
        
        ans = 0
        for index in range(0, len(s) - 1):
            ans += abs(ord(s[index]) - ord(s[index+1]))
        
        return ans