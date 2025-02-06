#exercice d'algorithmique : somme des nombres entiers entre deux bordes qui devront être saisi

val1 = int(input("Entrez un nombre entier = "))
val2 = int(input("Entrez un nombre entier = "))

somme = 0
for k in range (val1, val2+1):
    somme = somme + k
print("La somme des nombres entre " + str(val1) + " et " + str(val2) + " = ", somme)
