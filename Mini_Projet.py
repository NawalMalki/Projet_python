# Nom et Prenom : Malki Nawal 




#Fonction qui affiche le menu principal
def principal_menu():
    print("*****************************  MENU **************************************************")
    print("*                 0.  Quitter                                                        *")
    print("*                 1.  Merge Sort                                                     *")
    print("*                 2.  Heap Sort                                                      *")
    print("*                 3.  Triangle de Pascal                                             *")
    print("*                 4.  Tours de Hanoi                                                 *")
    print("*                 5.  Multiplication de matrices                                     *")
    print("*                 6.  Arbres AVL                                                     *")
    print("**************************************************************************************")

# 1 Merge Sort
 # Version itérative
def merge_sort_iter(T):
    sous_tab = [] #sous_tab contiendra tous les elements de T en tant que des listes [[elt1],[elt2],..]
    for x in T:
        sous_tab.append([x])

    while len(sous_tab) > 1:
         resultat = []
         for i in range(0, len(sous_tab), 2):
             if i + 1 < len(sous_tab):
                 T1 = sous_tab[i]
                 print(T1)
                 T2 = sous_tab[i + 1]
                 print(T2)
                 merged = merge(T1, T2)
                 resultat.append(merged)
             else:
                 resultat.append(sous_tab[i])
         sous_tab = resultat

    return sous_tab[0]
def merge(A, B):
    merged = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):

        if A[i] < B[j]:

            merged.append(A[i])
            i += 1
        else:

            merged.append(B[j])
            j += 1

    while i < len(A):
        merged.append(A[i])
        i += 1

    while j <len(B):
        merged.append(B[j])
        j += 1
    print(merged)
    print("----------------------------------------------")
    return merged

# Version recursive
# 3 étapes : Diviser , Résoudre , recombiner ( Du principe : diviser pour regner )
def merge_sort_rec(Tab):
    if len(Tab) <= 1:
        print(Tab,end=" ")
        return Tab
    milieu = len(Tab) // 2
    # Etape 1 : Diviser
    T1 = Tab[:milieu]
    print(T1,end=" ")
    T2 = Tab[milieu:]
    print(T2)
    # Diviser chaque séquence du tableau en des sous séquences
    T1 = merge_sort_rec(T1)
    T2 = merge_sort_rec(T2)
    # Etape 2 et 3  : Resoudre et Recombiner les sous résultats ( solutions )
    return merge(T1, T2)

# 2 Heap Sort
 # La seule différence entre le min et le max heap sort se situe au niveau de rendre le tableau soit max ou min heap ( la fonction heapify)
def Heap_sort(Tab,x):
    if x==2:
        print("---------------Etape1 : Creation du max heap -------------------------")
    else :
        print("---------------Etape1 : Creation du min heap -------------------------")
    # On commence par créer un max ou min heap à partir du tableau saisi
    for i in range(len(Tab) // 2, -1, -1):
        if x == 2:
            Heapify_max(Tab, i)
        if x == 1:
            Heapify_min(Tab,i)
    if x == 2:
        print("-----------------Tableau sous forme de max heap ---------------------")
    else:
        print("-----------------Tableau sous forme de min heap ---------------------")
    print(Tab)

    # On supprime la racine à chaque fois jusqu'à supprimer toutes les racines
    tableau_res = []
    print("----------------Etape2 :Suppressions successives des racines ------------")
    while Tab:
        tableau_res.append(Supprime_racine(Tab, x))


    return tableau_res

#Fonction qui fixe le max heap
def Heapify_max(T, i):
    n = len(T)
    fils_gauche = 2 * i + 1
    fils_droit = 2 * i + 2
    racine = i
    #La valeur de la racine doit être toujours plus grande que ses fils
    if fils_gauche < n and T[fils_gauche] > T[racine]:
        racine = fils_gauche
        print(T)
    if fils_droit < n and T[fils_droit] > T[racine]:
        racine=fils_droit
        print(T)
    if racine != i:
        T[i], T[racine] = T[racine], T[i]
        print(T)
        Heapify_max(T, racine)

#Fonction qui fixe le min heap
def Heapify_min(T, i):
    n=len(T)
    fils_gauche = 2 * i + 1
    fils_droit = 2 * i + 2
    racine = i
    # La valeur de la racine doit toujours être plus petite que ses fils
    if fils_gauche < n and T[fils_gauche] < T[racine]:
        racine = fils_gauche
        print(T)
    if fils_droit < n and T[fils_droit] < T[racine]:
        racine=fils_droit
        print(T)
    if racine != i:
        T[i], T[racine] = T[racine], T[i]
        print(T)
        Heapify_min(T, racine)

#La fonction qui supprime la racine du heap
def Supprime_racine(T,x):
    # On remplace la racine par le dernier element du tableau (indice -1)
    T[0], T[-1] = T[-1], T[0]

    element = T.pop() #pop retourne l element supprimé apres sa suppression de T
    print("On supprime la racine ",end=" ")
    print(element)
    if x==2:
        Heapify_max(T, 0)
    if x==1:
        Heapify_min(T,0)
    return element

# 3 . Triangle de Pascal
def Triangle_de_Pascal(N):
    tab=[1]
    temp=[]
    print("le triangle de pascal de ", N , "lignes")
    for i in range(N):
        for j in range(len(tab)):
            print(tab[j],end=" ")
        print()
        temp.append(1)
        for j in range(len(tab)-1):
            temp.append(tab[j]+tab[j+1])
        temp.append(1)
        tab=temp
        temp=[]

# 4 Tours de Hanoi
def Tours_de_hanoi(n, A, B,C):
    if n == 1:
        print("Passer le disque 1 de ", A, "a", C)
        Affichage_graphiqueHanoi(n, A ,B, C)
        return
    Tours_de_hanoi(n - 1, A, B, C)
    print("Passer le disque ", n, " de ", A, " a ", C)
    Affichage_graphiqueHanoi(n, A, B, C)
    Tours_de_hanoi(n - 1, A, B, C)

def Affichage_graphiqueHanoi(n, A, B, C):
    # Print the pegs
    for i in range(n):
        print("       ---  ", end=" ")
    print()
    print("------------ ", end=" ")
    print("------------ ", end=" ")
    print("------------ ")
    print("    ",A, end=" ")
    print("           ", B, end=" ")
    print("           ", C,"      ")
    print( )

# 5. Multiplication de deux matrices
# Multiplication classique
def Multiplication_classique(A, B):
    if len(A[0]) != len(B):
        print("On ne peut multiplier deux matrices que si les dimensions sont compatibles ( Nbre de c(1)=Nbre de l(2))")
# la matrice resultat : Lignes (= nbre de lignes de A ) , Colonnes (=Nbre de colonnes de B)
    resultat = []
    # On intialise resultat par 0
    for ligne in range(len(A)):
        resultat.append([0] * len(B[0]))


    # Traitement
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultat[i][j] += A[i][k] * B[k][j]
            Affichage_Matrice(resultat)
            print("------------")
    return resultat

  # Affichage de la matrice
def Affichage_Matrice(T):
    larg = []
    for ligne in T:
        for x in ligne:
            larg.append(len(str(x)))
    max_larg = max(larg)

    for ligne in T:
        for x in ligne:
            print(f"{x:>{max_larg}}", end=" ")
        print()
    #print("--------------")

 # Creation de la matrice ( Demander a l'utilisateur de la saisir )
def Creer_matrix():
    dimension_string = input("Saisir la dimension de la matrice (Lignes /Colonnes ): ")  # L utilisateur saisie deux nombres
    dimensions = dimension_string.split()  # ça retourne une liste [ 'Nombre de lignes' , 'Nombre de colonnes' ]
    lignes = int(dimensions[0])  # ça correspond au Nombre de lignes ( commentaire ci dessus)
    colonnes = int(dimensions[1])  # ça correspond au Nombre de colonnes

    matrice = []
    for _ in range(lignes):
        lignes = []
        for x in input().split():
            lignes.append(int(x))

        #Ajouter la ligne qu'on vient de creer a la matrice
        matrice.append(lignes)

    return matrice
# Multiplication de Strassen
"""
Pour realiser la multiplication de Strassen j'ai suivi l'approche suivante :
(Sachant que la multiplication de Strassen ne se fait que pour les matrices carrés et de dimension divisible par 2)
J'ai crée plusieurs fonctions supplementaires pour m'aider qui sont : 
- Une fonction addition matrice qui fait la somme des matrices  element par element car : les expressions de Strassen contiennent ça 
- Une fonction soustraction qui fait la soustraction
- Une fonction subdivision qui divise la matrice donnée en resultat en quatre matrices et les retourne dans un tuple
- Une fonction fusion qui fusionne le resultat C ( car a la fin de la multiplication de Strassen on n'obtient que les sous matrices (c11,c12,..)
- La fonction Multiplication_de_Strassen fait appel a toutes ces fonctions pour un bon fonctionnement 

"""


# Fonction qui fait l'addition de deux matrices
def addition_matrices(A, B):
    C = []
    for i in range(len(A)):
        ligne = []
        for j in range(len(A[i])):
            ligne.append(A[i][j] + B[i][j])
        C.append(ligne)
    return C

# Fonction qui fait la soustraction de deux matrices


def soustraction_matrices(A, B):
    C = []
    for i in range(len(A)):
        ligne = []
        for j in range(len(A[i])):
            ligne.append(A[i][j] - B[i][j])
        C.append(ligne)
    return C

# Fonction qui subdivise la matrice en quatre sous matrices de taille n/2



def Subdivision(M):
    n = len(M)
    a = []
    # L operateur // donne le resultat entier du quotient
    for i in range(n // 2):
        ligne = []
        for j in range(n // 2):
            ligne.append(M[i][j])
            # Ligne aura M[0][0] , M[0][1] pour la 1ere iteration de i
            # i est fixé et j est entrain de parcourir
        a.append(ligne)  # La matrice a est remplie donc ligne par ligne
    b = []
    for i in range(n // 2):
        ligne = []
        for j in range(n // 2, n):
            ligne.append(M[i][j])
        b.append(ligne)
    c = []
    for i in range(n // 2, n):
        ligne = []
        for j in range(n // 2):
            ligne.append(M[i][j])
        c.append(ligne)
    d = []
    for i in range(n // 2, n):
        ligne = []
        for j in range(n // 2, n):
            ligne.append(M[i][j])
        d.append(ligne)
    return (a, b, c, d)


def Multiplication_de_strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        # On divise les matrices A et B ( chacune en quatre matrices de taille len/2)
        (A11, A12, A21, A22) = Subdivision(A)
        (B11, B12, B21, B22) = Subdivision(B)
        Affichage_Matrice(A11)
        print("-------------------------------------------------------------------------------------------------")
        Affichage_Matrice(A12)
        print("-------------------------------------------------------------------------------------------------")
        Affichage_Matrice(A21)
        print("-------------------------------------------------------------------------------------------------")
        Affichage_Matrice(A22)
        print("-------------------------------------------------------------------------------------------------")
        Affichage_Matrice(B11)
        print("-------------------------------------------------------------------------------------------------")
        Affichage_Matrice(B12)
        print("-------------------------------------------------------------------------------------------------")
        Affichage_Matrice(B21)
        print("-------------------------------------------------------------------------------------------------")
        Affichage_Matrice(B22)
        print("-------------------------------------------------------------------------------------------------")
    P1 = Multiplication_de_strassen(A11, soustraction_matrices(B12, B22))
    P2 = Multiplication_de_strassen(addition_matrices(A11, A12), B22)
    P3 = Multiplication_de_strassen(addition_matrices(A21, A22), B11)
    P4 = Multiplication_de_strassen(A22, soustraction_matrices(B21, B11))
    P5 = Multiplication_de_strassen(addition_matrices(A11, A22), addition_matrices(B11, B22))
    P6 = Multiplication_de_strassen(soustraction_matrices(A12, A22), addition_matrices(B21, B22))
    P7 = Multiplication_de_strassen(soustraction_matrices(A11, A21), addition_matrices(B11, B12))

    x = soustraction_matrices(P4, P2)
    y = addition_matrices(x, P6)
    c11 = addition_matrices(P5, y)
    Affichage_Matrice(c11)
    c12 = addition_matrices(P1, P2)
    Affichage_Matrice(c12)
    c21 = addition_matrices(P3, P4)
    Affichage_Matrice(c21)
    z = soustraction_matrices(P1, P3)
    a = soustraction_matrices(z, P7)
    c22 = addition_matrices(P5, a)
    Affichage_Matrice(c22)
    # La matrice resultat est C qui est aussi subdivisée en quatre sous matrices donc on doit les fusionner
    # return Fusion(c11, c12, c21, c22)
    return Fusion(c11, c12, c21, c22)

def Fusion(a, b, c, d):
    n = len(a)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(a[i][j])
        for j in range(n):
            ligne.append(b[i][j])
        resultat.append(ligne)   #On ajoute la ligne qu'on vient de creer a notre matrice resultat
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(c[i][j])
        for j in range(n):
            ligne.append(d[i][j])
        resultat.append(ligne)   #même principe
    return resultat


"""
Pour manipuler les AVL :
- Facteur d equilibre : qui calcule le facteur d'equilibre
- Reequilibrer : Qui equilibre l'arbre apres insertion ou suppression
- Rotation droite , Rotation gauche
- Calcul Hauteur : Qui calcule la hauteur du noeud et qui le stocke dans hauteur ( de la classe Noeud)
et d'autres 

"""
# Une classe noeud qui représente un noeud de l AVL sachant que chaque noeud a ( une cle , un fils gauche / droit , une hauteur)
class Noeud:
    def __init__(self, key):
        self.cle = key
        self.fgauche = None
        self.fdroit = None
        self.hauteur = 1

# Fonction qui retourne la hauteur du noeud passé en argument
def Hauteur(noeud):
    if not noeud:
        return 0
    return noeud.hauteur

# Calcul du facteur d equiblibre : Hauteur du sous arbre gauche - Hauteur du sous arbre droit
def Facteur_dequilibre(noeud):
    if not noeud:
        return 0
    return Hauteur(noeud.fgauche) - Hauteur(noeud.fdroit)



def Calcul_Hauteur(noeud):
    noeud.hauteur = max(Hauteur(noeud.fgauche), Hauteur(noeud.fdroit)) + 1

def Rotation_droite(noeud):
    fils_gauche = noeud.fgauche
    noeud.fgauche = fils_gauche.fdroit
    fils_gauche.fdroit = noeud
    Calcul_Hauteur(noeud)
    Calcul_Hauteur(fils_gauche)
    print("+ Rotation droite  en" , noeud.cle)
    return fils_gauche

def Rotation_gauche(noeud):
    fils_droit = noeud.fdroit
    noeud.fdroit = fils_droit.fgauche
    fils_droit.fgauche = noeud
    Calcul_Hauteur(noeud)
    Calcul_Hauteur(fils_droit)
    print("+ Rotation gauche en ",noeud.cle)
    return fils_droit

"""Cette fonction insertion fait les etapes d'insertion normale dans une BST :
On compare la cle donnée en argument a la racine et on se deplace a gauche ou a droite selon le resultat
Pourtant elle ne fait pas le reequilibrage de l'AVL ( C'est le rôle de la fonction Reequilibrer) . Cela aidera a clarifier la trace 
"""
def insertion(noeud, cle):
    if not noeud:
        return Noeud(cle)
    if cle < noeud.cle:
        noeud.fgauche = insertion(noeud.fgauche, cle)
        print("insertion de " , cle , "en sous arbre gauche")
        Affichage(noeud)
        print("---------------------------------")
    else:
        noeud.fdroit = insertion(noeud.fdroit, cle)
        print("Insertion de " , cle , "en sous arbre droit")
        Affichage(noeud)
        print("--------------------------------")

    Calcul_Hauteur(noeud)
    return noeud

def Suppression(noeud, val):
    if not noeud:
        return None

    if int(val) < noeud.cle:
        noeud.fgauche = Suppression(noeud.fgauche, val)
    elif int(val) > noeud.cle:
        noeud.fdroit = Suppression(noeud.fdroit, val)
    else:
        if not noeud.fgauche and not noeud.fdroit:
            return None
        elif not noeud.fgauche:
            return noeud.fdroit
        elif not noeud.fdroit:
            return noeud.fgauche

        min_node = Trouver_min(noeud.fdroit)
        noeud.cle = min_node.cle
        noeud.right = Suppression(noeud.fdroit, min_node.cle)

    Calcul_Hauteur(noeud)
    return noeud

def Trouver_min(noeud):
    courrant = noeud
    while courrant.fgauche:
        courrant = courrant.left
    return courrant

def Reequilibrer(noeud):
    if not noeud:
        return None

    Calcul_Hauteur(noeud)
    Eq = Facteur_dequilibre(noeud)

    if Eq > 1 and Facteur_dequilibre(noeud.fgauche) >= 0:
        return Rotation_droite(noeud)

    if Eq > 1 and Facteur_dequilibre(noeud.fgauche) < 0:
        noeud.fgauche = Rotation_gauche(noeud.fgauche)
        return Rotation_droite(noeud)

    if Eq < -1 and Facteur_dequilibre(noeud.fdroit) <= 0:
        return Rotation_gauche(noeud)

    if Eq < -1 and Facteur_dequilibre(noeud.fdroit) > 0:
        noeud.fdroit = Rotation_droite(noeud.fdroit)
        return Rotation_gauche(noeud)



# Affichage avec un parcours infixe
def Affichage(noeud):
    if not noeud :
        return

    Affichage(noeud.fgauche)
    print(noeud.cle)
    Affichage(noeud.fdroit)


#On commence par Afficher le menu principal avec la fonction : principal menu
principal_menu()
while True:
    a = int(input("Quel est votre choix ? "))
    if a == 0:
        break
    if a == 1:
        print("************************** MENU : MERGE SORT   ***************************************")
        print("*                  0.  Retour au menu principal                                      *")
        print("*                  1.  Approche itérative (Bottom-up)                                *")
        print("*                  2.  Approche récursive (Top-down)                                 *")
        print("**************************************************************************************")
        b = int(input("Quel est votre choix "))
        if b == 0:
            principal_menu()
        else :
            # L'utilisateur remplit le tableau a trier
            Tableau_a_traiter = []
            while True:
                valeur = input("Saisir une valeur ('q' pour terminer ): ")
                if valeur == 'q':
                    break
                valeur=int(valeur)
                Tableau_a_traiter.append(valeur)
            #Traitement : Version recursive
            if b == 2:
                print("********************** Approche récursive (Top-down) *********************************")
                print("*********************************** Tableau a trier  *********************************")
                print(Tableau_a_traiter)
                print("*********************************** Trace du Merge Sort  *****************************")
                A = merge_sort_rec(Tableau_a_traiter)
                print("**************************************** Resultat ************************************")
                print(A)
                principal_menu()
            # Traitement : version itérative
            if b==1:
                print("********************** Approche itérative (Bottom-up) ********************************")
                print("********************************* Tableau a trier  ***********************************")
                print(Tableau_a_traiter)
                print("******************************* Trace du Merge Sort  *********************************")
                A = merge_sort_iter(Tableau_a_traiter)
                print("************************************ Resultat ****************************************")
                print(A)
                principal_menu()

    elif a == 2:
        print("*********************  MENU : HEAP SORT **********************************************")
        print("*                  0.  Retour au menu principal                                      *")
        print("*                  1.  Min Heap Sort                                                 *")
        print("*                  2.  Max Heap Sort                                                 *")
        print("**************************************************************************************")
        print("Remarque : le max heap sort fait le tri du tableau en ordre decroissant ;             ")
        print("Le min heap sort fait le contraire : Tri le tableau dans l'ordre croissant  ;         ") 
        b = int(input("Quel est votre choix "))
        if b == 0:
            principal_menu()
        else :
            Tableau_a_traiter = []
            while True:
                valeur = input("Saisir une valeur ('q' pour terminer ): ")
                if valeur == 'q':
                    break
                valeur = int(valeur)
                Tableau_a_traiter.append(valeur)
            print("************************************ Tableau a trier  ********************************")
            print(Tableau_a_traiter)
            print("*********************************** Trace du Heap Sort  ******************************")
            A = Heap_sort(Tableau_a_traiter,b)
            print("*************************************** Resultat *************************************")
            print(A)
            principal_menu()

    elif a == 3:
        N = int(input("saisir le nombre pour le triangle de Pascal "))
        Triangle_de_Pascal(N)
        principal_menu()
    elif a == 4:
        print("***************************** MENU : TOURS DE HANOI  *********************************")

        m=int(input("Saisir le nombre de disques "))
        i = input("Nom de la colonne 1 ")
        j = input("Nom de la colonne 2 ")
        z=  input("Nom de la colonne 3 ")
        print("Regles du jeu : ")
        print("- Vous ne pouvez déplacer qu’un seul disque à la fois")
        print("- Vous ne pouvez pas placer un disque sur un disque plus petit que lui")
        print("- Ce parcours doit être réalisé en un minimum de coups")

        print("***************************** TRACE DE L ALGORITHME  *********************************")
        Tours_de_hanoi(m,i,j,z)

        principal_menu()
    elif a == 5:
        print("**************** MENU : MULTIPLICATION DE DEUX MATRICES ******************************")
        print("*                  0.  Retour au menu principal                                      *")
        print("*                  1.  Multiplication classique                                      *")
        print("*                  2.  Multiplication de Stressen                                    *")
        print("**************************************************************************************")
        b = int(input("Quel est votre choix "))
        if b == 0:
            principal_menu()
        else :
            print("Matrice 1 : ")
            matrix = Creer_matrix()
            print("Matrice 2 : ")
            matrix2 = Creer_matrix()
            print("************************ Matrices à multiplier ***************************************")
            Affichage_Matrice(matrix)
            print("--------")
            Affichage_Matrice(matrix2)
            if b==1:
                print("************************ Trace de la multiplication **********************************")
                A = Multiplication_classique(matrix, matrix2)
                print("********************************* Resultat *******************************************")
                Affichage_Matrice(A)
                principal_menu()
            if b==2:
                print("************************ Trace de la multiplication **********************************")
                A = Multiplication_de_strassen(matrix, matrix2)
                print("********************************* Resultat *******************************************")
                Affichage_Matrice(A)
                principal_menu()



    elif a == 6:
        print("********** MENU : AVL ( LES ARBRS BINAIRES DE RECHERCHE EQUILIBRES )******************")
        print("*                  0.  Retour au menu principal                                      *")
        print("*                  1.  Creation d'un AVL                                             *")
        print("*                  2.  Insertion d'un element                                        *")
        print("*                  3.  Suppression d un element                                      *")
        print("**************************************************************************************")
        b = int(input("Quel est votre choix "))
        if b == 0:
            principal_menu()
        else :
            if b==1:
                print("******************* 1.  Creation d'un AVL *********************************************")
                x = int(input("Saisir la premiere valeur qui definira l AVL "))
                racine = Noeud(x)
                Affichage(racine)
                principal_menu()
            elif b==2 :
                print("******************* 2.  Insertion d'un element ****************************************")
                x = int(input("Entrer la valeur a inserer dans l AVL ('q' pour quitter): "))
                racine = Noeud(x)
                def Creation_de_AVL(racine):
                    while True:
                        valeur = input("Entrer la valeur a inserer dans l AVL ('q' pour quitter): ")
                        if valeur == 'q':
                            break
                        racine = insertion(racine, int(valeur))
                    return racine



                racine = Creation_de_AVL(racine)
                print("Reequilibrage de l AVL  : -----------------------------------------------")
                racine = Reequilibrer(racine)
                print("l AVL que vous avez cree est : ------------------------------------------")
                Affichage(racine)
                principal_menu()
            else :
                print("******************* 3.  Suppression d un element **************************************")
                valeur = input("Entrer la valeur a supprimer de l AVL ('q' pour quitter): ")
                racine = Suppression(racine, valeur)
                print("l AVL apres suppresion de  :", valeur, " -------------------------------")
                Affichage(racine)
                principal_menu()
