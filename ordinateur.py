# ordinateur.py
import random
from arriere_boutique import victoire


def ordi(plateau):
    # Priorité : Bloquer le coup gagnant du joueur
    for ligne in range(3):
        for col in range(3):
            if plateau[ligne][col] == "⬛":
                plateau[ligne][col] = "🔵"
                if victoire(plateau, "🔵"):
                    return  # L'ordinateur a bloqué le coup gagnant du joueur
                else:
                    plateau[ligne][col] = "⬛"  # Annuler le coup
    # Si aucun coup gagnant à bloquer, jouer de manière aléatoire
    while True:
        ligne = random.randint(0, 2)
        col = random.randint(0, 2)
        if plateau[ligne][col] == "⬛":
            plateau[ligne][col] = "🔵"
            break
