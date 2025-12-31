# 2114. Maximum Number of Words Found in Sentences
# 2 mins to solve

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # traverse the array
        # split each sentence and find count
        # keep track of max count and return it

        count = 0
        for sentence in sentences:
            if count < len(sentence.split()):
                count = len(sentence.split())
        
        return count

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split()) for sentence in sentences)