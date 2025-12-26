def decode_string(s):
    ans = ""
    stack = []
    
    # stack
    # keep pushing until ]
    # if ] process everything till [ and numbers before
    # and push back to stack
    # traverse string till the end
    # pop everything generate ans
    
    # took 38 mins to solve
    
    for value in s:
        temp_str = ""
        temp_num = ""
        
        if value == "]":
            while stack and stack[-1] != "[":
                char = stack.pop()
                temp_str = char + temp_str  
            
            stack.pop()
            
            while stack and stack[-1].isnumeric():
                char = stack.pop()
                temp_num = char + temp_num
            
            temp_str = (int(temp_num) * temp_str)
            for val in temp_str:
                stack.append(val)
            
        else:
            stack.append(value)
        
    
    while stack:
        char = stack.pop()
        ans = char + ans
       
    return ans