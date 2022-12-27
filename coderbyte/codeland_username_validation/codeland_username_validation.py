def CodelandUsernameValidation(strParam):
    if len(strParam) < 4 or len(strParam) > 25:
        return False

    if strParam[len(strParam) - 1] == '_':
        return False

    if not (97 <= ord(strParam[0]) <= 122):
        return False

    for a in strParam:
        if not ((97 <= ord(a) <= 122) or (48 <= ord(a) <= 57) or ord(a) == 95):
            return False
    return True
