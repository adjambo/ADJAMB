def crypt(message):
    result = ""
    for char in message:
        result += chr(ord(char) + 1)  # Ne prend pas encore en compte "pas"
    return result