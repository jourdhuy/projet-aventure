import time

# Présentation du jeu et message de bienvenue
Welcome_message = print("Bienvenue sur Cybernétique Dystopie : Le Code de la Liberté")
Presentation_game = print(
    "Dans un futur cyberpunk, où une AI gouverne le monde, incarnez Nova qui est un hacker super doué. "
    "En découvrant un début de code, vous avez le début de la clé pour détruire Néotrons et libérer l'humanité "
)

# Aptitude pour joueur, code et barre de vie
code = []
compétance = ["hacking"]
Barre_de_vie = 100
hacking = 20


# Barre des attaques des ennemis
Drones_attaque = 15
Brigade_police_attaque = 25
Militaire_attaque = 25
neotons_attaque_nova=30

# Barre des vies des ennemis
Drones_barre_de_vie = 30
Police_barre_de_vie = 45
Militaire_barre_de_vie = 60
Néotrons_barre_de_vie=85

def game_over():
    print("Game Over. Vous avez perdu.")
    restart_game = input("Voulez-vous recommencer le jeu ? (Oui/Non) ").lower()
    if restart_game == "oui":
        reset_game()
    else:
        print("Merci d'avoir joué.")

def reset_game():
    global Barre_de_vie  
    Barre_de_vie = 100  
    print("Le jeu a été réinitialisé.")
    return datacenter_QG

# Début du jeu
def datacenter_QG():#1er partie du jeux 
    global Barre_de_vie  # Utilisation de la variable Barre_de_vie globalement

    Homme_mystérieux = "Nova: Je vois un vieux Datacenter, je pense que je vais aller explorer car il n'y a personne."
    print(Homme_mystérieux)
    time.sleep(2)

    Nova_explore = "Nova part explorer le Datacenter."
    print(Nova_explore)
    time.sleep(2)

    Nova_commentaire = "Nova: Cet endroit est vraiment pourri, je pense que je vais venir m'installer ici."
    print(Nova_commentaire)
    time.sleep(2)

    message_video = "Soudain, tous les datacenters et un écran s'allument pour lire une vidéo."
    print(message_video)
    time.sleep(2)

    homme_mystérieux = (
        "Homme mystérieux: Bonjour à vous cher humain, si vous êtes ici cela veut dire que vous êtes l'élite de la nation et même du monde.")
    print(homme_mystérieux)
    time.sleep(2)

    mission_message = "Moi et mon équipe avons découvert une faille pour détruire Néotrons avec une suite de combinaisons."
    print(mission_message)
    time.sleep(2)

    mission_message_continued = (
        "Votre mission ici est de chercher tous les bouts de codes. Je n'ai plus beaucoup de temps, je vous souhaite bonne chance, "
        "vous êtes les derniers espoirs de l'humanité."
    )
    print(mission_message_continued)
    time.sleep(2)

    object_pour_joueur = (
        "Vous avez une carte pour vous localiser et obtenir le reste du code pour détruire Néotron. "
        "Vous obtenez aussi la compétence de hacker."
    )
    print(object_pour_joueur)
    time.sleep(2) 
    carte_choix()
    
 # Fonction pour voyager dans toute la map
def carte_choix():
    carte_emplacement = "Sur la carte il y a plusieurs villes où il y a les différents codes : a) Silicon Valley\nb) Réseau clandestin\nc) Nigth City\nd) Cyber Nexus"
    print(carte_emplacement)
    time.sleep(2)
    #Demande au joueur où il veut aller et le raméne à la fonction qu'il veut 
    choix_ville_joueur = input("Où voulez-vous aller ? : ").lower()
    if choix_ville_joueur == "silicon valley" or choix_ville_joueur=="a":
        Silicon_Valley()
    elif choix_ville_joueur == "réseau clandestin" or choix_ville_joueur=="b":
        Réseau_clandestin()
    elif choix_ville_joueur == "nigth city" or choix_ville_joueur=="c":  # Correction de la faute de frappe
        Nigth_City()
    elif choix_ville_joueur == "Cyber Nexus" or choix_ville_joueur=="d":
        if len(code) == 3:   # Si le joueur a les 3 codes, lancer la fonction cyber_nexus
            cyber_nexus()
        else:
            print("Vous n'avez pas les codes nécessaires pour accéder à Cyber Nexus.")
            game_over()
    
        

def Silicon_Valley():
    global Barre_de_vie # Utilisation de la variable Barre_de_vie globalement
    global Drones_barre_de_vie # Utilisatio de la variable Drones_bar_de_vies

    Nova_arrive_silicon = print("Nova: Je viens enfin d'arriver à la Silicon Valley !")
    time.sleep(2)
    Nova_drones = print("Nova: Je vois au loin des Drones qui sont en train de s'approcher.")
    time.sleep(2)

    while Drones_barre_de_vie > 0 and Barre_de_vie > 0:

        indication_attaque = input(
            "Les Drones vous attaquent, que voulez-vous faire ?\n1: Attaque hacking\n2: Se soigner\n3: S'enfuir\n"
        )

        if indication_attaque == "1":
            # Attaque hacking sur les Drones
            Drones_barre_de_vie -= hacking
            print(f"Vous attaquez les Drones avec succès,il leurs reste {Drones_barre_de_vie}")

            # Ennemis attaquent
            Barre_de_vie -= Drones_attaque
            print(f"Les Drones vous attaquent et ils vous restent {Barre_de_vie} !")

        elif indication_attaque == "2":
            # Option de soin
            soin = 10  # Le joueur peut se soigner
            Barre_de_vie += soin
            print(f"Vous vous soignez et récupérez {soin} points de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Drones_attaque
            print(f"Les Drones vous attaquent et il vous restent {Barre_de_vie} de vie ")

        elif indication_attaque == "3":
            # S'enfuir (fin du combat)
            print("Vous ne pouvez pas vous enfuir, on n'aime pas les lâches")
            return game_over()

        # Vérifier si le joueur est toujours en vie
        if Barre_de_vie <= 0:
            print("Vous avez été vaincu. Game over.")
            return game_over()

        # Vérifier si les ennemis sont morts
        if Drones_barre_de_vie <= 0:
            print("Vous avez vaincu les Drones!")
        if Barre_de_vie <100: # Régénération de la vie du joueur jusqu'à 100
                while Barre_de_vie==100:
                    Barre_de_vie+1
                    return message_intro_altman
        elif Barre_de_vie==100:
            return message_intro_altman
        
    message_intro_altman = "Sam Altman: Bienvenue à toi, je'attendais ta visite "
    print(message_intro_altman)
    time.sleep(2)

    réponse_de_nova = "Nova: Mais qui êtes-vous monsieur ?"
    print(réponse_de_nova)
    time.sleep(2)

    réponse_de_altman = (
       "Sam Altman: Je suis Sam Altman et je suis le créateur de Néotrons et je voudrais te poser une énigme pour savoir")
    print(réponse_de_altman)
    time.sleep(10)
    
    réponse_de_altman_2=("si vous êtes digne d'avoir les secrets et le code pour détruire Néotrons ")
    print(réponse_de_altman_2)
    time.sleep(2)
    # Case enigme que le joueur doit répondre
    Enigme_altman = "Quelle est la date de création de l'ENIAC :"
    print(Enigme_altman)
    
    while True:  # Boucle pour répéter la question en cas de mauvaise réponse
        reponse_enigme_altman = (input("a) 1946\nb) 1976\nc) 1834\nChoisissez une lettre pour confirmer votre réponse: "))

        if reponse_enigme_altman == "a":
            bonne_reponse_altman = "Sam Altman: Bravo, vous avez réussi l'épreuve !"
            print(bonne_reponse_altman)
            time.sleep(2)

            bonne_reponse_altman_2 = "Sam Altman: Le code est 111"
            print(bonne_reponse_altman_2)
            time.sleep(2)

            code.append(111)
            return carte_choix()  # Retourne sur la carte pour que le joueur puisse choisir une autre zone
        else:
            mauvaise_réponse_altman = "Sam Altman:Tu t'es trompé,réssaye !!."
            print(mauvaise_réponse_altman)
            time.sleep(2)

        
def Réseau_clandestin():
    global Barre_de_vie# Utilisation de la variable Barre_de_vie globalement
    global Drones_barre_de_vie# Utilisation de la variable Drones_barre_de_vie globalement
    global Drones_attaque
    
    arriver_nova = "Nova:Après des heures, je suis enfin arrivée au Réseau Clandestin"
    time.sleep(2)
    print(arriver_nova)
    
    description_de_nova="Nova:J'ai vu que sur la carte que la prochaine personne est dans cette zone"
    time.sleep(2)
    print(description_de_nova)
    
    description_de_nova_2="Nova:Je vois que dans cette zone il y'a beaucoup de SDF alors que un peux plus long il y'a des énormes building avec des véhicules volants !"
    time.sleep(2)
    print(description_de_nova_2)
    
    ennemis_nova="Je vois au loins des drones,je pense que ils m'ont vu !!!"
    time.sleep(3)
    print(ennemis_nova)
    
    while Drones_barre_de_vie > 0 and Barre_de_vie > 0:

        indication_attaque = input(
            "Les Drones vous attaquent, que voulez-vous faire ?\n1: Attaque hacking\n2: Se soigner\n3: S'enfuir\n"
        )

        if indication_attaque == "1":
            # Attaque hacking sur les Drones
            Drones_barre_de_vie -= hacking
            print(f"Vous attaquez les Drones avec succès,il leurs reste {Drones_barre_de_vie}")

            # Ennemis attaquent
            Barre_de_vie -= Drones_attaque
            print(f"Les Drones vous attaquent et ils vous restent {Barre_de_vie} !")

        elif indication_attaque == "2":
            # Option de soin
            soin = 10  # Le joueur peut se soigner
            Barre_de_vie += soin
            print(f"Vous vous soignez et récupérez {soin} points de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Drones_attaque
            print(f"Les Drones vous attaquent et il vous restent {Barre_de_vie} de vie ")

        elif indication_attaque == "3":
            # S'enfuir (fin du combat)
            print("Vous ne pouvez pas vous enfuir, on n'aime pas les lâches")
            return game_over()

        # Vérifier si le joueur est toujours en vie
        if Barre_de_vie <= 0:
            print("Vous avez été vaincu. Game over.")
            return game_over()

        # Vérifier si les ennemis sont morts
        if Drones_barre_de_vie <= 0:
            print("Vous avez vaincu les Drones!")
        # Régénération de la vie du joueur jusqu'à 100
            if Barre_de_vie <100:
                while Barre_de_vie==100:
                    Barre_de_vie+1
                    return arriver_pearce
            elif Barre_de_vie==100:
                return arriver_pearce
    
    arriver_pearce="Après cette bataille contre les drones, Aiden Pearce le plus célébre hacker de Chigago vient rejoindre Nova"
    print(arriver_pearce)
    time.sleep(2)
    
    dialogue_pearce_nova="Aiden Pearce:Je vois que tu as du talent Nova\nje vais te demander de me suivre pour aller dans un endroit plus sur"
    print(dialogue_pearce_nova)
    time.sleep(2)
    
    réponse_nova_pearce="Nova:Mais comment je pourrais vous faire confiance,je ne vous connait pas "
    print(réponse_nova_pearce)
    time.sleep(2)
    
    réponse_pearce_nova_2="Aiden Pearce: J'ai oubliée de me présenter je suis Aiden Pearce"
    print(réponse_pearce_nova_2)
    time.sleep(2)
    
    réponse_nova_pearce_2="Nova: Mais non vous etes Aiden Pearce qui fait partie de la Dedsec"
    print(réponse_nova_pearce_2)
    time.sleep(2)
    
    réponse_pearce_nova_3="Aiden Pearce: Néotrons au début a était conçu pour faire le bien dans le monde\nmais à cause des USA, Néotrons a était déployés pour faire la police et elle s'est rebellé ! "
    print(réponse_pearce_nova_3)
    time.sleep(2)
    
    énigme_de_pearce="Aiden Pearce: Je vais te poser une question pour savoir si tu es apte à avoir le code pour détruire Néotrons"
    print(énigme_de_pearce)
    time.sleep(2)
    
    énigme_de_pearce_2 = "Quel est le système d'exploitation le plus utilisé dans le monde :"
    print(énigme_de_pearce_2)
    time.sleep(2)

    while True:  #une boucle  pour répéter la question si il y'a une mauvaise réponse
        réponse_énigme = input("a) linux\nb) windows\nc) macOS\nChoisis une lettre pour confirmer ta réponse: ")

        if réponse_énigme == "linux" or réponse_énigme=="a":
            message_énigme = "Aiden Pearce: Je vous félicite pour avoir trouvé l'énigme, donc je peux vous faire confiance pour le code qui est 110"
            print(message_énigme)
            time.sleep(2)

            message_final = "Aiden Pearce: Je vous souhaite bonne chance, car vous êtes notre dernière espoir pour délivrer l'humanité"
            print(message_final)
            time.sleep(2)

            code.append(110)#rajoute dans la liste le code 
            return carte_choix()
        else:
            mauvaise_réponse_pearce = "Aiden Pearce: Tu t'es trompé,réssaye !"
            print(mauvaise_réponse_pearce)#si il y a une mauvaise réponse on va réenvoyer à la réponse énigme 
            time.sleep(2)


def Nigth_City():
    global Brigade_police_attaque
    global Drones_attaque
    global Drones_barre_de_vie
    global Police_barre_de_vie
    global Barre_de_vie
    global hacking

    arriver_nigth_city = "Nova: Après quelques heures de voyage avec mon véhicule, je suis enfin arrivé dans cette ville !"
    print(arriver_nigth_city)
    time.sleep(2)

    descriptions_nigth_city = "Nova: Dans cette ville, il y a plein de publicités sur tous les buildings de la ville. "
    print(descriptions_nigth_city)
    time.sleep(2)

    descriptions_nigth_city_2 = "Nova: J'ai entendu par une personne que dans cette ville tout le monde a du matériel cybernétique.\nLe monde est contrôlé par l'intelligence artificielle pour acheter plus de produits."
    print(descriptions_nigth_city_2)
    time.sleep(2)

    mission_nova = "Nova: Ma mission est de retrouver la prochaine personne pour essayer d'avoir un des morceaux de code pour détruire cette IA."
    print(mission_nova)
    time.sleep(2)

    dicussion_nova = "Nova: Depuis que j'ai découvert cette vidéo, je suis recherché par tout le monde."
    print(dicussion_nova)
    time.sleep(2)

    nova_repere = "Policiers: Les gars je crois que j'ai vu un mec qui est recherché par le gouvernement, si on réussit à l'attraper on pourra avoir une prime."
    print(nova_repere)
    time.sleep(2)

    message_attaque = "Lancement du combat: "
    print(message_attaque)
    time.sleep(2)
    while  Police_barre_de_vie > 0 and Barre_de_vie > 0:
        indication_attaque = input(
            "Les Drones et la police vous attaquent, que voulez-vous faire :\n1: Attaque hacking\n2: Se soigner\n3: S'enfuir\n")

        if indication_attaque == "1":
            # Attaque hacking sur police
            Police_barre_de_vie -= hacking
            print(
                f"Vous attaquez la police avec succès, il leur reste {Police_barre_de_vie} à la police."
            )

            # Attaque ennemis
            Barre_de_vie -=  Brigade_police_attaque
            print(
                f"la police vous attaquent, il vous reste {Barre_de_vie} de vie."
            )

        elif indication_attaque == "2":
            # Soin
            soin = 10  #    l   e joueur peut se soigner
            Barre_de_vie += soin
            print(f"Vous vous soignez et récupérez {soin} points de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Brigade_police_attaque
            print(
                f"La police vous attaquent, il vous reste {Barre_de_vie} de vie."
            )

        elif indication_attaque == "3":
            # S'enfuir (fin du combat)
            print("Vous ne pouvez pas vous enfuir, on n'aime pas les lâches")
            return game_over()

        # Vérifier si le joueur est toujours en vie
        if Barre_de_vie <= 0:
            print("Vous avez été vaincu.")
            return combat_perdu()

    # Combat terminé, vérifier qui est vaincu
    if  Police_barre_de_vie <= 0:
        print("Vous avez vaincu la police!")
        return combat_gagné()
    elif  Police_barre_de_vie > 0:
        print("Vous avez vaincu les Drones, mais la police vous a capturé.")
        return combat_perdu()
    


def combat_gagné():
    nova_combat_reusis = "Nova: C'était difficile de les vaincre !"
    print(nova_combat_reusis)
    time.sleep(2)

    intro_silverhand = "SilverHand: Je trouve que tu te bats bien petit, avant tout je me présente je suis Johnny SilverHand, le vieux rocker."
    print(intro_silverhand)
    time.sleep(2)

    nova_réponse = "Nova: Mais nonnnnn, c'est bien vous !"
    print(nova_réponse)
    time.sleep(2)

    silverhand_reponse = "SilverHand: Et ouais c'est bien moi, bref je veux te poser une question pour voir si tu es apte à avoir le code pour détruire cette IA."
    print(silverhand_reponse)
    time.sleep(2)
    return enigme()


def enigme():
    while True:
        silverhand_enigme = input(
            "SilverHand: Comment s'appelait l'ancêtre de l'Internet, créé par le département américain de la défense?\n a) Arpanet\n b) Minitel\n c) Ethernet\n"
        )
        print(silverhand_enigme)
        time.sleep(2)
        if silverhand_enigme.lower() == "arpanet" or silverhand_enigme.lower() == "a":
            bonne_reponse = "SilverHand: Je te félicite d'avoir trouvé l'énigme, maintenant je peux te faire confiance pour le code qui est 11110100010."
            print(bonne_reponse)
            time.sleep(2)

            message_final = "SilverHand: Petit, je te souhaite bonne chance pour réussir à combattre cette méchante IA."
            print(message_final)
            time.sleep(2)
            code.append(11110100010)  # rajoute dans la liste le code
            return carte_choix()
        else:
            mauvaise_reponse_pearce = "SilverHand: Tu es trop nul, réessaye !"
            print(mauvaise_reponse_pearce)  # Si c'est une mauvaise réponse, on renvoie à la question de l'énigme
            time.sleep(2)


def combat_perdu():
    nova_réveille = "Nova: Arhhhhhh, j'ai mal à la tête."
    print(nova_réveille)
    time.sleep(2)

    deckars_réponse = "Rick Deckars: Comment vas-tu, tu t'es pris une grosse raclée !"
    print(deckars_réponse)
    time.sleep(2)

    nova_reponse = "Nova: Je commence à aller mieux, mais vous êtes Rick Deckars."
    print(nova_reponse)
    time.sleep(2)

    deckars_réponse_2 = "Deckars: Je vais te dire quelques trucs par rapport à Néotrons."
    print(deckars_réponse_2)
    time.sleep(2)

    nova_reponse_2 = "Nova: Mais vous n'allez pas me tuer car vous êtes un réplicant !"
    print(nova_reponse_2)
    time.sleep(2)

    deckars_réponse_3 = "Deckars: Ne vous inquiétez pas, je ne suis pas là pour vous tuer, mais là pour vous aider.\nNéotrons a été créé par une grande entreprise qui avait plusieurs micro-entreprises.\n Ils avaient corrompu tout le gouvernement pour qu'il crée une intelligence artificielle, mais l'intelligence artificielle s'est rebellée et a hacké tous les serveurs de la terre."
    print(deckars_réponse_3)
    time.sleep(2)

    deckars_réponse_4 = "Deckars: Je pense que je vais te ramener chez Johnny pour qu'il te donne le code et que tu aides l'humanité."
    print(deckars_réponse_4)
    time.sleep(2)

    nova_reponse_3 = "Nova: Merci Beaucoup Deckars, vous m'avez beaucoup aidé !!!!"
    print(nova_reponse_3)
    time.sleep(2)

    return silverhand_seconde()


def silverhand_seconde():
    intro_silverhand = "SilverHand: Deckars m'a parlé de toi et que tu es un hacker incroyable, avant tout je me présente je suis Johnny SilverHand, le vieux rocker."
    print(intro_silverhand)
    time.sleep(2)

    nova_réponse = "Nova: Mais nonnnnn, c'est bien vous !"
    print(nova_réponse)
    time.sleep(2)

    silverhand_reponse = "SilverHand: Et ouais c'est bien moi, bref je veux te poser une question pour voir si tu es apte à avoir le code pour détruire cette IA."
    print(silverhand_reponse)
    time.sleep(2)

    return enigme()

def cyber_nexus():
    global Barre_de_vie
    global Brigade_police_attaque
    global Police_barre_de_vie
    global hacking
    global Militaire_attaque
    global Militaire_barre_de_vie
    global code
    global Néotrons_barre_de_vie
    global neotons_attaque_nova
    global Jeux_gagné

    if len(code) < 3:
        print("Vous avez besoin de 3 codes pour accéder à Cyber Nexus.")
        carte_choix()

    nova_arriver_cyber = "Nova: Nous sommes enfin dans Cyber Nexus pour contrer Neutrons et libérer l'humanité."
    print(nova_arriver_cyber)
    time.sleep(2)

    nova_description_cyber = "Nova: Il y a un grand gratte-ciel avec plein de policiers autour de ce bâtiment."
    print(nova_description_cyber)
    time.sleep(2)

    nova_attaque = "Nova: Je pense que je vais les attaquer pour rentrer dans le bâtiment."
    print(nova_attaque)
    time.sleep(2)

    nova_attaque_2 = "Nova part attaquer la Brigade policière."
    print(nova_attaque_2)
    time.sleep(2)

    Brigade_police = "Policiers: FAITES ATTENTION, IL Y A LE SUSPECT QUI NOUS ATTAQUE !!!!"
    print(Brigade_police)
    time.sleep(2)

    while Police_barre_de_vie > 0 and Barre_de_vie > 0:
        indication_attaque = input(
            "Les Policiers vous attaquent, que voulez-vous faire ?\n1: Attaque hacking\n2: Se soigner\n3: S'enfuir\n"
        )

        if indication_attaque == "1":
            # Attaque hacking sur les policiers
            Police_barre_de_vie -= hacking
            print(f"Vous attaquez les Policiers avec succès, il leur reste {Police_barre_de_vie} de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Brigade_police_attaque
            print(f"Les Policiers vous attaquent et il vous reste {Barre_de_vie} de vie.")

        elif indication_attaque == "2":
            # Option de soin
            soin = 10  # Le joueur peut se soigner
            Barre_de_vie += soin
            print(f"Vous vous soignez et récupérez {soin} points de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Brigade_police_attaque
            print(f"Les Policiers vous attaquent et il vous reste {Barre_de_vie} de vie.")

        elif indication_attaque == "3":
            # S'enfuir (fin du combat)
            print("Vous ne pouvez pas vous enfuir, on n'aime pas les lâches.")
            game_over()

        # Vérifier si le joueur est toujours en vie
        if Barre_de_vie <= 0:
            print("Vous avez été vaincu. Game over.")
            game_over()

        # Vérifier si les ennemis sont morts
        if Police_barre_de_vie <= 0:
            print("Vous avez vaincu la Brigade policière!")
            # Régénération de la vie du joueur jusqu'à 100
            while Barre_de_vie < 100:
                Barre_de_vie += 1

    nova_entre_batiment = "Nova: Je vais enfin rentrer dans ce bâtiment, je vois qu'il y a un ascenseur au bout du couloir."
    print(nova_entre_batiment)
    time.sleep(2)

    nova_ascenseur = "Nova prend l'ascenseur."
    print(nova_ascenseur)
    time.sleep(2)

    militaire_qui_attaque = "Nova: Je vois des militaires devant la porte."
    print(militaire_qui_attaque)
    time.sleep(2)

    militaire_react = "Militaire: Tuez-le !!!!!!"
    print(militaire_react)
    time.sleep(2)

    while Militaire_barre_de_vie > 0 and Barre_de_vie > 0:
        indication_attaque_militaire = input(
            "Les Militaires vous attaquent, que voulez-vous faire ?\n1: Attaque hacking\n2: Se soigner\n3: S'enfuir\n"
        )

        if indication_attaque_militaire == "1":
            # Attaque hacking sur les militaires
            Militaire_barre_de_vie -= hacking
            print(f"Vous attaquez les Militaires avec succès, il leur reste {Militaire_barre_de_vie} de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Militaire_attaque
            print(f"Les Militaires vous attaquent et il vous reste {Barre_de_vie} de vie!")

        elif indication_attaque_militaire == "2":
            # Option de soin
            soin = 10  # Le joueur peut se soigner
            Barre_de_vie += soin
            print(f"Vous vous soignez et récupérez {soin} points de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Militaire_attaque
            print(f"Les Militaires vous attaquent et il vous reste {Barre_de_vie} de vie!")

        elif indication_attaque_militaire == "3":
            # S'enfuir (fin du combat)
            print("Vous ne pouvez pas vous enfuir, on n'aime pas les lâches.")
            game_over()

        # Vérifier si le joueur est toujours en vie
        if Barre_de_vie <= 0:
            print("Vous avez été vaincu. Game over.")
            game_over()

    nova_entre_batiment = "Nova: J'ai enfin réussi à tuer les militaires, je pense que je vais aller vers le hall principal."
    print(nova_entre_batiment)
    time.sleep(2)

    choix_2_salles = input("Nova: Je vois qu'il y a deux salles.\na) Salle des serveurs\nb) Salle électrique\nOù voulez-vous aller : ")
    print(choix_2_salles)
    time.sleep(2)

    if choix_2_salles.lower() == "salle des serveurs" or choix_2_salles.lower() == "a":
        salle_serveurs()
    else:
        electrocution = "Vous arrivez dans la salle électrique."
        print(electrocution)
        time.sleep(2)
        electrocution("Vous vous faites électrocuter, n'oubliez pas que vous êtes conducteur.")
        game_over()

def salle_serveurs():
    global Barre_de_vie
    global Brigade_police_attaque
    global Police_barre_de_vie
    global hacking
    global Militaire_attaque
    global Militaire_barre_de_vie
    global code
    global Néotrons_barre_de_vie
    global neotons_attaque_nova

    arriver = "Nova: Je suis enfin arrivé dans la salle des serveurs mais il y a plein de policiers."
    print(arriver)
    time.sleep(2)

    policier_arriver = "Policier: Attrapez-le et tuez-le."
    print(policier_arriver)
    time.sleep(2)

    while Police_barre_de_vie > 0 and Barre_de_vie > 0:
        indication_attaque = input(
            "Les Policiers vous attaquent, que voulez-vous faire ?\n1: Attaque hacking\n2: Se soigner\n3: S'enfuir\n"
        )

        if indication_attaque == "1":
            # Attaque hacking sur les policiers
            Police_barre_de_vie -= hacking
            print(f"Vous attaquez les Policiers avec succès, il leur reste {Police_barre_de_vie} de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Brigade_police_attaque
            print(f"Les Policiers vous attaquent et il vous reste {Barre_de_vie} de vie.")

        elif indication_attaque == "2":
            # Option de soin
            soin = 10  # Le joueur peut se soigner
            Barre_de_vie += soin
            print(f"Vous vous soignez et récupérez {soin} points de vie.")

            # Ennemis attaquent
            Barre_de_vie -= Brigade_police_attaque
            print(f"Les Policiers vous attaquent et il vous reste {Barre_de_vie} de vie.")

        elif indication_attaque == "3":
            # S'enfuir (fin du combat)
            print("Vous ne pouvez pas vous enfuir, on n'aime pas les lâches.")
            game_over()

        # Vérifier si le joueur est toujours en vie
        if Barre_de_vie <= 0:
            print("Vous avez été vaincu. Game over.")
            game_over()

        # Vérifier si la police est morte
        if Police_barre_de_vie <= 0:
            print("Vous avez vaincu la Brigade policière!")
            # Régénération de la vie du joueur jusqu'à 100
            while Barre_de_vie < 100:
                Barre_de_vie += 1

    policer_vaincu = "Nova: J'ai réussi à les tuer, il faut que je rentre dans la salle des serveurs !!!"
    print(policer_vaincu)
    time.sleep(2)

    arrivage_serveurs = "Vous arrivez dans la salle des serveurs où il y a l'intelligence artificielle."
    print(arrivage_serveurs)
    time.sleep(2)

    dialogue_néotrons = "Néotrons: Enfin on se retrouve Nova, je t'observe depuis des années."
    print(dialogue_néotrons)
    time.sleep(2)

    dialogue_néotrons_2 = "Néotrons: Je t'attendais depuis des années pour te nuire à ton objectif de sauver l'humanité."
    print(dialogue_néotrons_2)
    time.sleep(2)

    dialogue_nova = "Nova: Je vais te détruire et je vais rendre et sauver la liberté de l'humanité."
    print(dialogue_nova)
    time.sleep(2)

    combat_annonce = "Vous entrez en combat avec Néotrons pour sauver l'humanité."
    print(combat_annonce)
    time.sleep(2)

    while Néotrons_barre_de_vie > 0 and Barre_de_vie > 0:
        indication_attaque_neutrons = input(
            "Les Neutrons vous attaquent, que voulez-vous faire ?\n1: Attaque hacking\n2: Se soigner\n3: S'enfuir\n"
        )

        if indication_attaque_neutrons == "1":
            # Attaque hacking sur les Neutrons
            Néotrons_barre_de_vie -= hacking
            print(f"Vous attaquez les Neutrons avec succès, il leur reste {Néotrons_barre_de_vie} de vie.")

            # Ennemis attaquent
            Barre_de_vie -= neotons_attaque_nova
            print(f"Les Neutrons vous attaquent et il vous reste {Barre_de_vie} de vie.")

        elif indication_attaque_neutrons == "2":
            # Option de soin
            soin = 10  # Le joueur peut se soigner
            Barre_de_vie += soin
            print(f"Vous vous soignez et récupérez {soin} points de vie.")

            # Ennemis attaquent
            Barre_de_vie -= neotons_attaque_nova
            print(f"Les Neutrons vous attaquent et il vous reste {Barre_de_vie} de vie.")

        elif indication_attaque_neutrons == "3":
            # S'enfuir (fin du combat)
            print("Vous ne pouvez pas vous enfuir, on n'aime pas les lâches.")
            game_over()

        # Vérifier si le joueur est toujours en vie
        if Barre_de_vie <= 0:
            print("Vous avez été vaincu. Game over.")
            game_over()

    # Vérifier si Néotrons est mort
    if Néotrons_barre_de_vie <= 0:
        print("Vous avez vaincu les Neutrons!")
        Jeux_gagné = True
        print("Vous avez réussi à sauver l'humanité et à rendre sa liberté.")
        time.sleep(2)

        fin_jeu = "Je vous remercie d'avoir joué à notre jeu !!!!!"
        print(fin_jeu)
        time.sleep(2)

        
        
datacenter_QG()



