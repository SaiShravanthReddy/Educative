def str_to_int(input_str):
    ans = 0

    index = len(input_str) - 1
    base = 1

    while index >= 0:
        if ord(input_str[index]) == 45:
            return -ans

        ans = ans + (base * (ord(input_str[index]) - 48))

        base *= 10
        index -= 1

    return ans

print(str_to_int("123"))