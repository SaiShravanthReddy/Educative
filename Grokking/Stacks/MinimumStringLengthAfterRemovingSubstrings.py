# Using strings
# 2 mins to solve

def min_length__using_str(s):
    
    while "AB" in s or "CD" in s:
        s = s.replace("AB", "")
        s = s.replace("CD", "")
    
    return len(s)

# Using stacks
# 7 mins to solve

def min_length(s):
    # Create stack
    # keep pushing chars into stack
    # if we encounter B or D, check prev for A or C and pop if there is a match
    # cal len of string
    # return

    stack = []

    for char in s:
        if char == "B" and len(stack) and stack[-1] == "A":
            stack.pop()
        elif char == "D" and len(stack) and stack[-1] == "C":
            stack.pop()
        else:
            stack.append(char)

    
    return len(stack)