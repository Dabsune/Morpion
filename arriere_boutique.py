
def changement(choix, plateau, joueur):
    case = {"A1": (0, 0), "A2": (1, 0), "A3": (2, 0),
            "B1": (0, 1), "B2": (1, 1), "B3": (2, 1),
            "C1": (0, 2), "C2": (1, 2), "C3": (2, 2)}
    if choix in case:
        ligne, col = case[choix]
        if plateau[ligne][col] == "⬛":  # vérification que la case est vide
            plateau[ligne][col] = joueur
            return True
        else:
            print("⚠️ Cette case a déjà été jouée. Choisissez une autre case.")
            return False
    else:
        print("⚠️ Il faut jouer dans la grille\nA1 A2 A3\nB1 B2 B3\nC1 C2 C3")
        return False


def victoire(plateau, joueur):
    # vérification des lignes
    for ligne in plateau:
        if all(case == joueur for case in ligne):
            return True
    # vérification des colonnes
    for col in range(3):
        if all(plateau[ligne][col] == joueur for ligne in range(3)):
            return True
    # vérification des diagonales
    if all(plateau[i][i] == joueur for i in range(3)):
        return True
    if all(plateau[i][2 - i] == joueur for i in range(3)):
        return True

    return False


def egalite(plateau):
    for ligne in plateau:
        for case in ligne:
            if case == "⬛":
                return False
    return True
