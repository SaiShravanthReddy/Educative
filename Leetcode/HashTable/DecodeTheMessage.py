# 2325. Decode the Message
# 12 mins to read and solve

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # print(ord("a")) - 97
        # char(97)

        hashmap = dict()
        count = 97
        for val in key:
            if val in hashmap:
                continue
            elif val == " ":
                continue
            else:
                hashmap[val] = count
                count += 1
        

        ans = ""
        for msg in message:
            if msg == " ":
                ans += " "
            else:
                ans += chr(hashmap[msg])

        return ans

# without ord() or char()
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        
        for char in message:
            res += mapping[char]
                
        return res