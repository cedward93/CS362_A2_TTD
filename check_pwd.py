
def check_pwd(pwd: str) -> bool:
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    has_lower = False
    for letters in pwd:
        if letters.islower():
            has_lower = True
    if has_lower is False:
        return False
    return True
