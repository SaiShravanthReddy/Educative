def valid_subarrays(nums):
    # Can do better - took 28 mins
    
    # create a stack
    # check posible subarrays at each index
    # count them
    # add them to total count
    
    stack = []
    
    count = 0
    index = 0
    
    while index < len(nums):
        
        if not stack:
            stack.append(nums[index])
            count += 1
            continue
        
        if nums[index] < stack[-1]:
            while stack:
                stack.pop()
                
            stack.append(nums[index])
            count += 1
            continue
        else: 
            tmp_index = index
            
            while tmp_index < len(nums) and nums[tmp_index] >= stack[-1]:
                stack.append(nums[tmp_index])
                count += 1
                
                tmp_index += 1
            
            while stack:
                stack.pop()
               
        index += 1
    
    return count
