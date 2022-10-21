        #ecrit les chiffres dans une liste
list = [int(x) for x in input("entrez une liste de nombre").split()]

        #creer une deuxieme liste pour afficher les nombres paires
listepaire=[]

        #place dans la liste
place=0

        #nombres d'éléments dans la liste
nb_elements=len(list)

        #le nombre qui est testé
nb_observé=0

        #tant que tout les chiffres n'ont pas été testé
while place != nb_elements:
        #prend la valeur du chiffre en position [place] dans la liste
    nb_observé=(list[place])
    
    if nb_observé % 2 == 0:
        #ajoute le nombre a la liste de nombre paire
        listepaire.append(nb_observé)

    place= place+1
        #affiche la liste des nombres paires
print("Nombres paires de la liste : ",listepaire)