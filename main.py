from arriere_boutique import changement, victoire, egalite
from ordinateur import ordi

while True:
    plateau = [["⬛" for _ in range(3)] for _ in range(3)]
    joueur = ["❌", "🔵"]
    tour = 0

    while True:
        mode = input("\033[1m" + f"\nTHE AMZAING NEW SUPER MORPION U DELUXE - ULTIMATE PYTHON EDITION" + "\033[0m"
                     + "\n\nVeux-tu jouer en solo ou en duo ?\n[1] solo - [2] duo\n")
        mode = mode.lower()
        if mode not in ["solo", "duo", "s", "d", "1", "2", "q"]:
            print("J'crois q'la question est mal répondue.\n")
        else:
            break

    while True:
        if (mode in ["1", "solo", "s"]) and tour == 1:
            ordi(plateau)
        else:
            while True:
                print("\033[1m" + f"\nTour de {joueur[tour]}" + "\033[0m")
                print(plateau[0])
                print(plateau[1])
                print(plateau[2])
                choix = input("Choisis une case [A1 => C3]: ")
                choix = choix.upper()
                if changement(choix, plateau, joueur[tour]):
                    break

        if victoire(plateau, joueur[tour]):
            print("\033[1m" + f"\n🎉 ET C'EST UNE VICTOIRE POUR : {joueur[tour]}" + "\033[0m")
            print(plateau[0])
            print(plateau[1])
            print(plateau[2])
            break
        elif egalite(plateau):
            print("\033[1m" + "\n🎲 C'EST UN MATCH NUL !" + "\033[0m")
            print(plateau[0])
            print(plateau[1])
            print(plateau[2])
            break

        tour = (tour + 1) % 2

    if mode in ["1", "solo", "s"]:
        recommencer = input("\nVeux-tu rejouer ?\n[1] oui - [autre] non\n")
        recommencer.lower()
        if recommencer not in ["oui", "o", "1"]:
            break
    else:
        recommencer = input("\nVoulez-vous rejouer ?\n[1] oui - [autre] non\n")
        recommencer.lower()
        if recommencer not in ["oui", "o", "1"]:
            break
