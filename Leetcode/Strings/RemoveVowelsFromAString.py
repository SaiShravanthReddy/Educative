# 1119. Remove Vowels from a String

class Solution:
    def removeVowels(self, s: str) -> str:
        vol = "aeiou"

        for char in vol:
            s = s.replace(char,"")

        return s
        

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiou')
        return ''.join(x for x in s if x not in vowels)