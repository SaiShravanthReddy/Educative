from stack import Stack

def reverse_string(stack, input_str):
    for index in range(len(input_str)):
        stack.push(input_str[index])
    
    rev_str = ""

    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))

input_str = "Educative"
print(input_str[::-1])