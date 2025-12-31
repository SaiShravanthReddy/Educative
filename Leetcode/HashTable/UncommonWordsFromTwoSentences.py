# 884. Uncommon Words from Two Sentences
# 7 mins to solve

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # convert str to list of words
        # keep track of freq of words
        # dont add in answer if appears more than once

        s1 = s1.split()
        s2 = s2.split()

        hashmap = dict()

        for word in s1:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 1
        
        for word in s2:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 1

        ans = []
        for val in hashmap:
            if hashmap[val] == 1:
                ans.append(val)
        
        return ans
