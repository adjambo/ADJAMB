def affiche():
    resultat = ""
    for i in range(1, 101):
        if i % 15 == 0:
            resultat += "FrisBee"
        elif i % 3 == 0:
            resultat += "Fizz"
        elif i % 5 == 0:
            resultat += "Buzz"
        else:
            resultat += str(i)
    return resultat
