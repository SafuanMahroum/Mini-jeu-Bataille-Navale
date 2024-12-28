'''Programme qui permet de jouer à la bataille navale contre l'ordinateur'''
'''Mahroum Safuan 1ére1'''

from random import randint
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

# Initialisation du plateau de jeu   [GRILLE]
n = 16
p = 16

tableau = []

for x in range(n):
    tableau.append(["O"] * p)

# Initialisation de la grille numpy
grille = np.zeros((n, p), dtype=int)

# Fonction pour afficher le plateau de jeu
def print_tableau(tableau):
    for ligne in tableau:
        print(" ".join(ligne))

# Création de l'image de la grille de jeu
noir = (220,20,60)
blanc = (30,144,255)
figure = Image.new("RGB", (p, n), blanc)

# Fonction pour placer les bateaux aléatoirement   [BATEAUX]
def random_ligne(tableau):
    return randint(0, len(tableau) - 1)

def random_colonne(tableau):
    return randint(0, len(tableau[0]) - 1)

# Creations des bateaux
bateaux = [ {"taille": 4, "symbole": "A"},
            {"taille": 3, "symbole": "B"},
            {"taille": 3, "symbole": "C"},
            {"taille": 2, "symbole": "D"},
            {"taille": 2, "symbole": "E"} ]

for bateau in bateaux:
    bateau_place = False

    while not bateau_place:
        bateau_ligne = random_ligne(tableau)
        bateau_colonne = random_colonne(tableau)
        orientation = randint(0, 1)

        # Vérifier si l'emplacement est libre pour le bateau
        emplacement_libre = True
        for i in range(bateau["taille"]):
            if orientation == 0:
                if bateau_colonne + i >= p or tableau[bateau_ligne][bateau_colonne + i] != "O":
                    emplacement_libre = False
                    break
            else:
                if bateau_ligne + i >= n or tableau[bateau_ligne + i][bateau_colonne] != "O":
                    emplacement_libre = False
                    break

        # Placer les bateaux sur le plateau de jeu
        if emplacement_libre:
            for i in range(bateau["taille"]):
                if orientation == 0:
                    tableau[bateau_ligne][bateau_colonne + i] = bateau["symbole"]
                    grille[bateau_ligne][bateau_colonne + i] = 1
                else:
                    tableau[bateau_ligne + i][bateau_colonne] = bateau["symbole"]
                    grille[bateau_ligne + i][bateau_colonne] = 1

            bateau_place = True

# Initialisation du nombre de bateaux coulés
bateaux_coules = 0
total_bateaux = len(bateaux)

# Boucle principale du jeu   [JEU]
tours = 0
bateaux_coules = 0

while bateaux_coules < len(bateaux):
    tours += 1
    print("Tour", tours)

    # Demande au joueur de deviner où sont placés les bateaux de l'ordinateur
    deviner_ligne = int(input("Choisir une Ligne - (entre 1 et 16) :")) - 1
    deviner_colonne = int(input("Choisir une Colonne - (entre 1 et 16) :")) - 1

    # Vérifier si le joueur a touché un bateau
    if grille[deviner_ligne][deviner_colonne] == 1:
        print("Bravo! Vous avez coulé un bateau de l'adversaire.")
        bateaux_coules += 1
        tableau[deviner_ligne][deviner_colonne] = "X"
    else:
        # Vérification des coordonées
        if (deviner_ligne < 0 or deviner_ligne >= n) or (deviner_colonne < 0 or deviner_colonne >= p): #Dépassemet
            print("Cette position n'est pas dans le plateau de jeu.")

        elif tableau[deviner_ligne][deviner_colonne] == "X": #Répetition
            print("Vous avez déjà essayé cette position.")

        else: #Si il na pas adeviné
            print("Dans l'éau!")
            tableau[deviner_ligne][deviner_colonne] = "X"

    # Mise à jour de l'image de la grille de jeu
    figure.putpixel((deviner_colonne, deviner_ligne), noir)
    plt.imshow(figure)
    plt.show()

print("Vous avez gagné la partie en", tours, "tours !")