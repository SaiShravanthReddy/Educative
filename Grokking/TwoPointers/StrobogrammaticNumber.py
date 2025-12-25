def is_strobogrammatic(num):
    hashmap = {
        "0": "0",
        "1": "1",
        "2": "NA",
        "3": "NA",
        "4": "NA",
        "5": "NA",
        "6": "9", 
        "7": "NA",
        "8": "8", 
        "9": "6"
    }
    
    start = 0
    end = len(num) - 1
    
    while start <= end:
        if hashmap[num[start]] != num[end]:
            return False
        
        start += 1
        end -= 1
    
    return True