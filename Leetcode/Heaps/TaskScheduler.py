# 621. Task Scheduler
# Medium
# Looked at hint and solution

# use max_heap and queue to solve
# use timer to see when cool down for a char is available
from collections import Counter, heapq, deque 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = []

        for _, freq in count.items():
            heapq.heappush(max_heap, -freq)
        
        time = 0

        q = deque()

        while max_heap or q:
            if max_heap: 
                freq = heapq.heappop(max_heap) + 1

                if freq != 0:
                    q.append([freq, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

            time += 1

        return time        
    
# one small bug in the above solution. 
# I process from time t = 0
# time 0 -> A
# time 1 -> idle/other
# time 2 -> idle/other
# time 3 -> A again

# subtle but important change

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = []

        for _, freq in count.items():
            heapq.heappush(max_heap, -freq)
        
        time = 0

        q = deque()

        while max_heap or q:
            time += 1

            if max_heap: 
                freq = heapq.heappop(max_heap) + 1

                if freq != 0:
                    q.append([freq, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time 
    
#This does
# time 1 -> A
# time 2 -> idle/other
# time 3 -> idle/other
# time 4 -> A again