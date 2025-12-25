# Using Arrays

class MyQueue(object):

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x):
        stk2_len = len(self.stk2)
        if stk2_len != 0:
            while stk2_len > 0:
                self.stk1.append(self.stk2.pop())
                stk2_len -= 1
            
        self.stk1.append(x)
        print("push", self.stk1, self.stk2)
        
        return

    def pop(self):
        stk1_len = len(self.stk1)
        if stk1_len != 0:
            while stk1_len > 0:
                self.stk2.append(self.stk1.pop())
                stk1_len -= 1
                
        print("pop", self.stk1, self.stk2)        
        return self.stk2.pop()

    def peek(self):
        stk1_len = len(self.stk1)
        if stk1_len != 0:
            while stk1_len > 0:
                self.stk2.append(self.stk1.pop())
                stk1_len -= 1
        
        print("peek", self.stk1, self.stk2) 
        return self.stk2[-1]

    def empty(self):
        if len(self.stk1) == 0 and len(self.stk2) == 0:
            return True
        
        return False
    
# from stack import Stack

# # Help on Stack in module stack object:
# # class Stack(builtins.object)
# #  |  Methods defined here:
# #  |  
# #  |  __init__(self)
# #  |      Initialize self.  See help(type(self)) for accurate signature.
# #  |  
# #  |  is_empty(self)
# #  |  
# #  |  pop(self)
# #  |  
# #  |  push(self, value)
# #  |  
# #  |  size(self)
# #  |  
# #  |  top(self)
# #  |  
# #  |  ----------------------------------------------------------------------
# #  |  Data descriptors defined here:
# #  |  
# #  |  __dict__
# #  |      dictionary for instance variables (if defined)
# #  |  
# #  |  __weakref__
# #  |      list of weak references to the object (if defined)

# class MyQueue(object):

#     def __init__(self):
#         self.stk1 = Stack()
#         self.stk2 = Stack()

#     def push(self, x):
#         stk2_len = self.stk2.size()
#         if stk2_len != 0:
#             while stk2_len > 0:
#                 self.stk1.push(self.stk2.pop())
#                 stk2_len -= 1
            
#         self.stk1.push(x)
#         print("push", self.stk1, self.stk2)
        
#         return

#     def pop(self):
#         stk1_len = self.stk1.size()
#         if stk1_len != 0:
#             while stk1_len > 0:
#                 self.stk2.push(self.stk1.pop())
#                 stk1_len -= 1
                
#         print("pop", self.stk1, self.stk2)        
#         return self.stk2.pop()

#     def peek(self):
#         stk1_len = self.stk1.size()
#         if stk1_len != 0:
#             while stk1_len > 0:
#                 self.stk2.push(self.stk1.pop())
#                 stk1_len -= 1
        
#         print("peek", self.stk1, self.stk2) 
#         return self.stk2.top()

#     def empty(self):
#         if self.stk1.size() == 0 and self.stk2.size() == 0:
#             return True
        
#         return False