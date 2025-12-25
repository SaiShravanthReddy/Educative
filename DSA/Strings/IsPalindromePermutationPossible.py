# We check if the given string can be use to make a palindrome or not

def is_palin_perm(input_str):
    # take string, remove spaces
    # lower case everything
    # hashmap strings
    # if odd, let one char freq be odd
    # if even, let no char freq be odd

    new_str = input_str.replace(" ", "").lower()
    length_str = len(new_str)

    odd = 0
    if length_str%2 != 0:
        odd = 1

    hashmap = {}

    for value in new_str:
        if value in hashmap:
            hashmap[value] += 1 
        else:
            hashmap[value] = 1

        
    for value in hashmap:
        if hashmap[value]%2 != 0:
            odd -= 1
            if odd == -1:
                return False

    return True


palin_perm = " ABABACCDDDD"
not_palin_perm = "This is not a palindrome permutation"

print(is_palin_perm(palin_perm))
print(is_palin_perm(not_palin_perm))