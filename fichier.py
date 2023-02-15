a = 5
b = 12
c=999
print(a*b)
print(a+b+c)


def syracuse():
    """
    fonction qui part d'un nombre
    donné par l'utilisateur et qui renvoie 
    le nombre d'étapes pour atteindre 1
    """
nb = int(input("Entrer un nombre positif supérieur à 0 : "))
cpt = 0 # initialise le compteur d'étapes à 0
while nb != 1: # tant que 1 nest pas atteint :
    if nb%2:
        nb=nb//2 # si nbre entré est pair, on le divise par 2
    else :
        nb=3*nb*+1 # si nbre entré est impair, on le multiplie par 3 et on ajoute 1
    cpt+=1 # on incrémente le compteur d'étapes
    print(nb)
    # break
print("Il a fallut", cpt, " étapes pour atteindre 1")

syracuse()
