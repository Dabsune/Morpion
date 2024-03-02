
import random


# affichage du plateau du morpion
def affichage(jeu):
    print('    A  B  C')
    for case, ligne in enumerate(jeu, start=1):
        print(str(case) + ' ', end=' ')
        print(' '.join(ligne))


# mise à jour du plateau selon le choix du joueur/ordi
def changement(choix, plateau, joueur):
    case = {"A1": (0, 0), "A2": (1, 0), "A3": (2, 0),
            "B1": (0, 1), "B2": (1, 1), "B3": (2, 1),
            "C1": (0, 2), "C2": (1, 2), "C3": (2, 2)}
    if choix in case:
        ligne, col = case[choix]
        if plateau[ligne][col] == "⬛":  # vérification que la case soit vide
            plateau[ligne][col] = joueur
            return True
        else:
            print("⚠️ Cette case a déjà été jouée. Choisis-en une autre.")
            return False
    else:
        print("⚠️ Il faut jouer dans la grille [A1 <> C3]")
        return False


# l'ordinateur (1 joueur)
def ordi(plateau):
    # priorité : bloquer les coups gagnants du joueur
    for ligne in range(3):
        for col in range(3):
            if plateau[ligne][col] == "⬛":
                plateau[ligne][col] = "❌"
                # vérifie si le coup du joueur mène à la victoire
                if victoire(plateau, "❌"):
                    plateau[ligne][col] = "🔵"
                    return
                else:
                    plateau[ligne][col] = "⬛"

    # Si il n'y aucun coup gagnant à bloquer, l'ordi joue aléatoirement
    while True:
        ligne = random.randint(0, 2)
        col = random.randint(0, 2)
        if plateau[ligne][col] == "⬛":
            plateau[ligne][col] = "🔵"
            break


# vérifie si une des conditions de victoires à été remplie
def victoire(plateau, joueur):
    # lignes
    for ligne in plateau:
        if all(case == joueur for case in ligne):
            return True
    # colonnes
    for col in range(3):
        if all(plateau[ligne][col] == joueur for ligne in range(3)):
            return True
    # diagonales
    if all(plateau[case][case] == joueur for case in range(3)):
        return True
    if all(plateau[case][2 - case] == joueur for case in range(3)):
        return True
    return False


# met fin à la partie s'il personne n'a gagné ni ne peut jouer
def egalite(plateau):
    for ligne in plateau:
        for case in ligne:
            if case == "⬛":
                return False
    return True
