
import def_room

while True:
    # paramètres initiaux de la partie
    plateau = [["⬛" for _ in range(3)] for _ in range(3)]
    joueur = ["❌", "🔵"]
    tour = 0
    num_tour = 1
    # choix du mode de jeu
    while True:
        mode = input("\033[1m" + f"\nTHE AMAZING NEW SUPER MORPION U DELUXE - ULTIMATE PYTHON EDITION" + "\033[0m"
                     + "\n\nVeux-tu jouer en solo ou en duo ? [1] solo - [2] duo\n")
        mode = mode.lower()
        if mode not in ["solo", "duo", "s", "d", "1", "2", "q"]:
            print("J'crois q'la question est mal répondue.\n")
        else:
            break

    while True:
        # activation du script de l'ordi (1 joueur)
        if (mode in ["1", "solo", "s"]) and tour == 1:
            def_room.ordi(plateau)
        # tour du/des joueur·s
        else:
            while True:
                if mode in ["1", "solo", "s"]:
                    print("\033[1m" + f"\nTour n°{num_tour}" + "\033[0m")  # numéro du tour en en solo
                else:
                    print("\033[1m" + f"\nTour de {joueur[tour]}" + "\033[0m")  # joueur à l'action en duo
                def_room.affichage(plateau)
                choix = input("Choisis une case: ")
                choix = choix.upper()
                if def_room.changement(choix, plateau, joueur[tour]):
                    break
        # si les conditions de fin de parties sont réunies
        if def_room.victoire(plateau, joueur[tour]):
            print("\033[1m" + f"\n🎉 ET C'EST UNE VICTOIRE POUR : {joueur[tour]}"
                  + "\033[0m" "\n(" + str(num_tour), "tours)")
            def_room.affichage(plateau)
            break
        elif def_room.egalite(plateau):
            print("\033[1m" + "\n🎲 MATCH NUL !" + "\033[0m", "\n(" + str(num_tour), "tours)")
            def_room.affichage(plateau)
            break
        # transition 0-1 pour savoir qui joue
        tour = (tour + 1) % 2
        # incrémentation du compteur une fois que les 2 personnes ont joué
        if tour == 0:
            num_tour += 1

    if mode in ["1", "solo", "s"]:
        recommencer = input("\nVeux-tu rejouer ? [1] oui - [autre] non\n")
        recommencer.lower()
        if recommencer not in ["oui", "o", "1"]:
            break
    else:
        recommencer = input("\nVoulez-vous rejouer ? [1] oui - [autre] non\n")
        recommencer.lower()
        if recommencer not in ["oui", "o", "1"]:
            break
