class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 23 mins to read and solve
        # Difficulty - Medium
        
        # two pointers - O(n^2)

        # set - O(n + n^2)
        # traverse array first, keep track of index with ball
        # add mod of ball - index to get ans array

        seen = set()

        for index in range(0, len(boxes)):
            if boxes[index] == "1":
                seen.add(index)
        
        ans = [0] * len(boxes)
        for index in range(0, len(ans)):
            for item in seen:
                ans[index] += abs(index - item)
        
        return ans
        