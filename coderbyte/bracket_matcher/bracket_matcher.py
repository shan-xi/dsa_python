def BracketMatcher(strParam):
    p = 0
    for c in strParam:
        if c == "(":
            p += 1

        if c == ")":
            if p == 0:
                return 0
            p -= 1
    if p > 0:
        return 0
    else:
        return 1

# keep this function call here
# print(BracketMatcher(input()))
