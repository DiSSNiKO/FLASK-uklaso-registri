def lengthValid(x,str):
    if len(str)<x:
        return False
    return True
def emailValid(str):
    for i in str:
        if i == "@":
            return True
    return False