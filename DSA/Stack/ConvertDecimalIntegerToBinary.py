from stack import Stack

def convert_int_to_bin(dec_num):
  # Handle edge cases!
  if dec_num == 0:
    return 0

  bin_stack = Stack()
  
  while dec_num > 0:
    bin_stack.push(dec_num%2)
    dec_num = dec_num//2
  
  ans = ""
  while not bin_stack.is_empty():
    ans = ans + str(bin_stack.pop())
    
  return ans