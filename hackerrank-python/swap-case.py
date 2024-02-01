def swap_case(s):
    string = ""
    for char in s:
        if char.islower():
            string += char.upper()
        elif char.isupper():
            string += char.lower()
        else:
            string += char
    return string


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
