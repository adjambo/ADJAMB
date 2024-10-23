def crypt(message):
    result = ""
    for char in message:
        result += chr(ord(char) + 1)
    return result