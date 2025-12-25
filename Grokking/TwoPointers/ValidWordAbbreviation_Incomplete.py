def stringToNumAndPointer(abbrPointer, abbr):
    number = ""
    
    while abbrPointer < len(abbr):
        print("abbrPointer", abbrPointer)
        if abbr[abbrPointer].isnumeric(): 
            number = number + abbr[abbrPointer]
        else: 
            break
        
        abbrPointer += 1
    
    if number == "":
        return 0, abbrPointer
    else:
        return int(number), abbrPointer
 

def valid_word_abbreviation(word, abbr):
    # use two poitners, one for word and the other for abbr
    # traverse through abbr, get the number
    # traverse through those many chars in word and see if word + 1 matches, abbr + 1 char
    # if true, cool, otherwise return false
    
    abbrPointer = 0
    wordPointer = 0
    
    while abbrPointer < len(abbr):
        # check if chars in are same
        if abbr[abbrPointer].isalpha():
            if word[wordPointer] != abbr[abbrPointer]:
                return False
                
        else: 
            wordPointer, abbrPointer = stringToNumAndPointer(abbrPointer, abbr)
            print("wordPointer, abbrPointer", wordPointer, abbrPointer)
            
        wordPointer += 1
        abbrPointer += 1

    return True
