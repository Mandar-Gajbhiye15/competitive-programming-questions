def swap_case(s):
    str1 = ""
    for i in range(len(s)):
        if s[i].isupper():
            str1 = str1+s[i].lower()
        elif s[i].islower():
            str1 = str1+s[i].upper()
        else:
            str1 = str1+s[i] 
    return str1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)