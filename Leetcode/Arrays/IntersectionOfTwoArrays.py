# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))
    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)

# https://www.geeksforgeeks.org/python/python-convert-set-into-a-list/

def intersect_sorted_array(A, B):
    # use two pointers

    i = 0
    j = 0

    ans = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 and A[i] != A[i-1]
                ans.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else: 
            j += 1

    
    return ans

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_array(A, B))