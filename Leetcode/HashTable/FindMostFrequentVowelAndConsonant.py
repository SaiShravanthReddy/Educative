# 3541. Find Most Frequent Vowel and Consonant

class Solution:
    def charFreq(self, char, hashmap):
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] += 1

        return hashmap[char]

    def maxFreqSum(self, s: str) -> int:
        # traverse the list 
        # use match case to add freq to hashmap
        # use another hashmap for const
        # find max in both and return
        hashmapV = dict()
        hashmapC = dict()
        max_v_freq = max_c_freq = 0

        for char in s:
            match char:
                case "a":
                    v_freq = self.charFreq(char, hashmapV)
                    if v_freq > max_v_freq:
                        max_v_freq = v_freq
                case "e":
                    v_freq = self.charFreq(char, hashmapV)
                    if v_freq > max_v_freq:
                        max_v_freq = v_freq
                case "i":
                    v_freq = self.charFreq(char, hashmapV)
                    if v_freq > max_v_freq:
                        max_v_freq = v_freq
                case "o":
                    v_freq = self.charFreq(char, hashmapV)
                    if v_freq > max_v_freq:
                        max_v_freq = v_freq
                case "u":
                    v_freq = self.charFreq(char, hashmapV)
                    if v_freq > max_v_freq:
                        max_v_freq = v_freq
                case _:
                    c_freq = self.charFreq(char, hashmapC)
                    if c_freq > max_c_freq:
                        max_c_freq = c_freq
    
        return max_v_freq + max_c_freq

# Much better
class Solution:
    def maxFreqSum(self, s: str) -> int:
        con = 0
        vow = 0
        d_set = set(s)
        for i in d_set:
            if i in "aeiou":
                vow = max(vow, s.count(i))
            else:
                con = max(con, s.count(i))
        return con+vow 