# 1331. Rank Transform of an Array
# Looked at solution
# 3 mins to write code

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # sort array, give ranks to numbers
        # traverse arr, retrive rank and create ans aray

        sorted_array = sorted(arr)
        hashmap = {}
        count = 1

        for val in sorted_array:
            if val not in hashmap:
                hashmap[val] = count
                count += 1
        
        ans = []
        for val in arr:
            ans.append(hashmap[val])
        
        return ans

# Time Complexity: O(N⋅logN)

# Sorting sortedArr takes O(N⋅logN) time. Iterating through arr and sortedArr 
# and inserting/looking up the rank for each number in our hash map takes in 
# total O(N⋅logN) time. Thus, the total time complexity is O(N⋅logN)



# Space complexity: O(N+S)

# Creating a copy of arr to be sorted will take O(N) time.

# The space taken by the sorting algorithm (S) depends on the language of implementation:

# 1. In Java, Arrays.sort() is implemented using a variant of the Quick Sort 
# algorithm which has a space complexity of O(logN).

# 2. In C++, the sort() function is implemented as a hybrid of Quick Sort, 
# Heap Sort, and Insertion Sort, with a worst-case space complexity of O(logN).

# 3. In Python, the sort() method sorts a list using the Timsort algorithm 
# which is a combination of Merge Sort and Insertion Sort and has a space complexity of O(N)
