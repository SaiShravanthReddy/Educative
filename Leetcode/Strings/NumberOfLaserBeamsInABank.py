# 2125. Number of Laser Beams in a Bank
# 7 mins to read and solve
# Medium

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Traverse each row and find count of 1s
        # multiply count r1 with count r2 and keep adding to final count
        #  return coutn

        ans = 0
        prev = 0
        cur = 0

        for val in bank:
            if val.count("1") > 0:
                cur = val.count("1")
                ans += prev*cur
                prev = cur

        return ans