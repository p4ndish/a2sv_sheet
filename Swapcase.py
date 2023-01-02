def swap_case(s):
    # s = s.split()
    res = ""
    for i in range(len(s)):
        # print(i)
        if s[i].isalpha():
            # print(s[i])
            if s[i].islower():
                res += s[i].upper()
            else:
                res += s[i].lower()
        else:
            res += s[i]
    return res
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
