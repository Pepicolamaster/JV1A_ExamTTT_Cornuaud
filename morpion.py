tableau=["-","-","-","-","-","-","-","-","-"]
tailleTableau=len(tableau)

#je défini comment placer un X
def placerX (monTableau,index1):
    j=0
    for j in range(tailleTableau):
        if(j==index1):
            tableau.pop(j)
            tableau.insert(j,"X")

#je défini comment placer un O
def placerO (monTableau,index1):
    j=0
    for j in range(tailleTableau):
        if(j==index1):
            tableau.pop(j)
            tableau.insert(j,"O")

#essai question 4 (grille complète)
def checkGrille(monTableau):
    j=0
    for j in range(tailleTableau):
        grilleIncomplète=False
        if(tableau[j]=="-"):
            grilleIncomplète=True

#je dessine mon tableau vide
for i in range(tailleTableau):
    if(i==2 or i==5 or i==8):
        print(tableau[i])
    else:
        print(tableau[i],end="")

pasVictoire=True
grilleIncomplète=True
while(pasVictoire and grilleIncomplète): #tant que la victoire n'est pas atteinte OU la grille est incomplète
    
    #Tour de J1
    checkGrille(tableau) #je vérifie que la grille est incomplète

    choixJ1=int(input("Dans quelle case de 0 à 8 souhaitez vous placer un X ?\n"))
    placerX(tableau,choixJ1) #j'appelle ma def pour placer un X

    #je redessine le tableau actualisé
    for i in range(tailleTableau):
        if(i==2 or i==5 or i==8):
            print(tableau[i])
        else:
            print(tableau[i],end="")

    #Tour de J2
    checkGrille(tableau) #je vérifie que la grille est incomplète

    choixJ2=int(input("Dans quelle case de 0 à 8 souhaitez vous placer un O ?\n"))
    placerO(tableau,choixJ2) #j'appelle ma def pour placer un O

    #je redessine le tableau actualisé
    for i in range(tailleTableau):
        if(i==2 or i==5 or i==8):
               print(tableau[i])
        else:
            print(tableau[i],end="")

if(grilleIncomplète==False):
    print("La grille est pleine !")
if(pasVictoire==False):
    print("Vous avez gagné !")

#essai de réponse à la question 6
#j"imagine que si l'on souhaite programmer un Puissance 4, il faudra tout d'abord changer la taille
#de la grille de jeu, et aussi redéfinir les conditions de victoire afin de déterminer si 4 même
#symboles sont alignés au lieu de trois. Sinon, le reste ne change pas : on cherche toujours à
#aligner horizontalement, vertiucalement ou en diagonale les symboles. On peut changer les X et O
#en J et R pour jaune et rouge, si on souhaite se rapprocher du Puissance 4.