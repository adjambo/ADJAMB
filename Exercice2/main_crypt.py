def crypt(message, pas=1):
    result = ""
    for char in message:
        result += chr(ord(char) + pas ) 
    return result


def decrypt(message, pas=1):
    result = ""
    for char in message:
        result += chr(ord(char) - pas)
    return result