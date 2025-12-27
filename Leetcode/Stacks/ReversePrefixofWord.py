#  Took 13 mins to solve

def reversePrefix(self, word: str, ch: str) -> str:
    # Traverse the str, and push to stack
    # untill we encounter ch
    # pop and store in rev-str
    #  and append with remaining str
    # if not found return original str

    if ch not in word:
        return word

    index = 0
    stk = []
    ans = ""

    while index < len(word) and word[index] != ch:
        stk.append(word[index])
        index += 1

    if index < len(word):
        stk.append(word[index])

    while stk:
        ans += stk.pop()

    ans = ans + word[index+1::1]


    return ans

# Best answer
def reversePrefix(self, word: str, ch: str) -> str:
        x= word.find(ch)
        if x !=-1:
            return word[:x+1][::-1]+word[x+1:]
        return word