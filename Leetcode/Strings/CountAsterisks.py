# 2315. Count Asterisks
# 8 mins to solve

class Solution:
    def countAsterisks(self, s: str) -> int:
        # traverse the array
        # keep a bool, bool = true when we see even |
        # bool starts with true
        # count *
        # return count

        ans = 0
        switch = True

        for char in s:
            if char == "|":
                switch = not switch
                
            if switch and char == "*":
                ans += 1
            
        return ans
    
    
class Solution:
    def countAsterisks(self, s: str) -> int:
        list1=s.split('|')
        print(list1)
        k=0
        for i in range(0,len(list1),2):
            str1=list1[i]
            k+=str1.count('*')
        return k