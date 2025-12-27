def array_advance(A):
    # 7 mins
    # keep track of max traversal using index and value
    # traverse the list
    # if index > max traversal 
    # return false

    max_traversal = 0
    index = 0

    while index < len(A):
        if index <= max_traversal:
            max_traversal = max(max_traversal, index + A[index])
            index += 1
        else:
            return False
    
    return True
    

    


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))