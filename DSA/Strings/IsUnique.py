def is_unique(input_str):
    print(set(input_str), len(set(input_str)), len(input_str))
    return len(set(input_str)) == len(input_str)