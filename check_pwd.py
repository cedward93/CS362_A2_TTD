
def check_pwd(pwd: str) -> bool:
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False

    # creating variables to test if elements are present in the string
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    symbols = "~`!@#$%^&*()_+-="

    # itterating through the string to search for elements
    for letters in pwd:
        if letters.islower():
            has_lower = True
        if letters.isupper():
            has_upper = True
        if letters.isdigit():
            has_digit = True
        if letters in symbols:
            has_symbol = True

    # verifying that the elements were indeed present
    if has_lower is False:
        return False
    if has_upper is False:
        return False
    if has_digit is False:
        return False
    if has_symbol is False:
        return False
    return True
