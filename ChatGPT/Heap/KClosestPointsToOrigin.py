import heapq

def kClosest(points, k):
    heap = []

    for point in points:

        if len(heap) >= k:
            heapq.heappushpop(heap, (-(point[0]*point[0] + point[1]*point[1]), point))
        else:
            heapq.heappush(heap, (-(point[0]*point[0] + point[1]*point[1]), point))

        print(heap)

    return [ coord for dist, coord in heap]


points = [[1,3],[-2,2],[5,8],[0,1]]
k = 2
print(kClosest(points, k))

# You are doing:
# always pushpop when size ≥ k

# But correct logic should be:
# only replace if the new point is closer than the farthest in heap


# Better solution

import heapq

def kClosest(points, k):
    heap = []

    for x, y in points:
        dist = x*x + y*y

        if len(heap) < k:
            heapq.heappush(heap, (-dist, [x, y]))
        else:
            if dist < -heap[0][0]:
                heapq.heapreplace(heap, (-dist, [x, y])) # pop then push

    return [point for _, point in heap]

# Time: O(n log k)
# Space: O(k)