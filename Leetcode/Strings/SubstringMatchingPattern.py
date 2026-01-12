# 3407. Substring Matching Pattern
# 16 mins to read, solve and debug edge cases
# Easy. 28% acceptance

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.split("*")

        if p[0] == "" and p[1] in s:
            return True
        
        if p[1] == "" and p[0] in s:
            return True
            
        if p[0] not in s:
            return False
        
        if p[1] not in s[s.index(p[0]) + len(p[0]) :]:
            return False
        
        return True

# str.find()
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        ss = p.split("*")
        if 0 == len(ss[0]):
            return -1 != s.find(ss[1])
        elif 0 == len(ss[1]):
            return -1 != s.find(ss[0])
        
        pos = s.find(ss[0])
        if -1 == pos:
            return False
        
        return -1 != s.find(ss[1], pos + len(ss[0]))

# str.rfind()
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        a, b = p.split('*')
        c = s.find(a)
        d = s.rfind(b)
        if c == -1 or d == -1:
            return False
        return c + len(a) <= d

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p_list = p.split('*')
        first = s.find(p_list[0])
        second = s.rfind(p_list[1])
        return first != -1 and second != -1 and first + len(p_list[0]) <= second