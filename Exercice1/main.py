def affiche(n1,n2):
    result = []
    for i in range(n1, n2 + 1):
        if i % 15 == 0:
            result.append("FrisBee")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return ''.join(result)


