def remove_duplicates(s):
    # define a stack
    # Check if stack is empty
    # if empty push
    # if not, peek and compare with next element
    # if same, pop element
    # if not push
    # continue till the end

    stk = []

    for value in s:
        if len(stk) == 0:
            stk.append(value)
        elif stk[-1] == value:
            stk.pop()
        else:
            stk.append(value)

    return "".join(stk)

print(remove_duplicates("sadkkdassa"))