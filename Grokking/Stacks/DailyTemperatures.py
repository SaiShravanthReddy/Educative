def daily_temperatures(temperatures):
  # create a new array of same length with all values set to 0
  # create a stack to keep track of the indices
  # traverse temp array, if value > index in stack, find dif and put it in new array
  length = len(temperatures)
  ans = [0] * length 
  
  stack = []
  stack.append(0)
  index = 1
  
  while index < len(temperatures):
    while stack and temperatures[stack[-1]] < temperatures[index]:
      ans[stack[-1]] = index - stack[-1]
      stack.pop()
    
    stack.append(index)
    
    index += 1


  return ans