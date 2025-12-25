def find_num_square(n):
    next_num = 0
    for value in str(n):
            next_num = next_num + (int(value) * int(value))
    
    return next_num


def is_happy_number(n):
    # set slow pointer to number
    # set fast pointer to square of numbers
    # incement slow pointer by 1
    # increment fast pointer by 2
    # if fast pointer points to 1 return true
    # if slow pointer = fast pointer return flase
    
    slow_ptr = n 
    fast_ptr = find_num_square(n) 
    
    while fast_ptr != 1 and slow_ptr != fast_ptr: 
        print(slow_ptr, fast_ptr)
        
        slow_ptr = find_num_square(slow_ptr)
        fast_ptr = find_num_square(find_num_square(fast_ptr))

    if fast_ptr == 1:
        return True
    else:
        return False