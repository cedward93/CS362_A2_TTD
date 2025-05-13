
def check_pwd(pwd: str) -> bool:
    if len(pwd) < 8:
        return False
    if len(pwd) > 20:
        return False
    return True
