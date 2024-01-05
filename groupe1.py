# Créé par Paul, le 04/12/2023 en Python 3.7

def histoire():
    '''L'histoire du jeu'''
    global lieu
    input("WARNING : CE PROGRAMME NE VOUS AIT PAS PROPOSE EN AUDIO-DESCRIPTION \n DE PLUS, CELUI-CI EST FORTEMENT PAR DES REFERENCES OBSCURES. \n (Aussi pour tout symptome de dégout en fin de jeu, moi, Paul, partage votre dégout mais n'est pas responsable) \n .Vous vous trouvez dans la ville de Levrille, une place tournante de la musique.\n Seulement, en arrivant, vous vous rendez compte que cette cité n'est plus ce qu'elle était...")
    lieu=lobby

def lobby():
    '''La ville'''
    global lieu
    reponse=input("\n4 chemins s'offrent alors à vous: le clochrer, le chrantier, le dojro et le skrate park.\nOù voulez vous aller pour découvrir ce qui c'est passé et pouvoir ainsi tout remettre en place ?")
    if reponse=="chrantier":
        lieu=chrantier
    elif reponse=="clochrer":
        lieu=clochrer
    elif reponse=="dojro":
        lieu=dojro
    elif reponse=="skrate park":
        lieu=skratepark

def skratepark():
    '''Rencontre avec Tony Hawk'''
    global lieu
    reponse=input("Vous arrivez au Skrate Park de Levrille/Lavrière. \n Vous croisez sur le Skrate Park Tony Hawk avec un skrate ainsi qu'un skrate sur le bord du skrate park. \n Si vous voulez faire un Kick-flip avec le skrate, tapez kick_flip \n Si vous voulez taper la discute avec Tony Hawk, tapez discute \n Pour revenir au centre vrille, tapez vrille")
    if reponse=="kick_flip": #Renvoie à la suite de l'aventure après avoir fait un Kick Flip
        lieu=Skrate2
    elif reponse=="discute" : #Renvoie au game over avec Tony Hawk
        lieu=GOTH
    elif reponse=='vrille':
        lieu=lobby

def GOTH():
    '''Game Over ou Tony Hawk te tue'''
    global lieu
    input("Tony Hawk n'est pas très commode... \n Votre comportement l'a tellement remonté qu'il vous assome avec son skrate... \n La blessure vous sera fatale, dommage...")
    lieu='perdu'

def Skrate2():
    '''Conversation avec Tony Hawk après le Kick Flip'''
    global lieu
    reponse=input("Tony Hawk te voit sur le bord du skrate après que t'aie fait ton Kick_Flip. \n <<Vous faites quoi ici ? C'est le Skrate Park de Tony Hawk privé ici ! Vous allez partir d'ici ! \n Enfin, mais qu'est ce qui vous a dit que vous pouviez venir ici ?>> \n Dans cette situation, que faites vous ? \n Pour refaire un kick flip avec votre skrate, tapez kick_flip \n Pour demander à Tony Hawk <<Ptdr T qui ?>>, tapez tqui")
    if reponse=='kick_flip': #Si le joueur refait un Kick_flip devant Tony Hawk, GAME OVER
        lieu=GOTH
    elif reponse=="tqui": #Si le joueur demande à Tony Hawk qui il est, il continue
        lieu=Skrate3

def Skrate3():
    '''Marché avec Tony Hawk'''
    global lieu
    global parchemrins
    reponse=input("Tony Hawk s'indigne de votre question mais se sent obligé de vous éduquer: \n <<Mais je suis Tony Hawk enfin, vous oseriez dire ça a un président ? \n Bon, vous pouvez rester si vous m'offrez une babiole... \n Ou alors... Vous renoncez à votre skate et je peux vous offrir une babiole... Le choix vous apartient.>> \n \n Que faire ? Vous cherchez dans vos poches et vous pensez qu'à une chose : \n - Lui donner un papier dans le fond de mon sac : taper papier \n - Lui redonner notre skrate et voir ce qu'il va nous donner: skrate")
    if reponse=='papier':
        if inventaire["Parchemrin de Daoine Antiel"]==0 and inventaire["Parchemrin de la Nonne"]==0:  #Si le joueur n'a pas de parchemrin, il ne peut pas le donner à Tony Hawk
            input("VOUS LUI AVEZ DONNÉ UN TICKET DE CAISSE... EST-CE QUE C'EST BON POUR VOUS?!")
            lieu=GOTH
        else : #Si le joueur a un parchemrin, alors il peut le donner à Tony Hawk
            lieu=GOPD
    elif reponse=='skrate' :
        lieu=PTH

def GOPD():
    '''Game over où le joueur donne un des parchemrins à Tony Hawk'''
    global lieu
    input("Tony Hawk reçoit le parchemrin et semble dire sous sa barbe <<Encore un des ces bidules là...>> \n Mais il vous autorise à faire du skrate avec lui \n Le soleil se couche et vous avez passé toute la journée au skrate park...  \n Dans un élan de précipitation, vous regardez ce que vous avez dans votre sac avant de voir que le papier que vous lui avait donné... \n était un de vos parchemrins... dommage...")
    lieu='perdu'

def PTH():
    '''Parchemin donné par Tony Hawk'''
    global lieu
    global inventaire
    input("Vous rendez le skrate à Tony Hawk, qui a l'air surpris \n <<Vous êtes plutôt accomodant, pour quelqu'un qui fait des Kick-flips... \n Bon, je vous avez promis un petit quelque chose, n'est-ce pas ?>> \n Il cherche dans son sac quelque chosev, et il s'agit d'un parchemrin ! \n <<Je lui trouve pas d'utilité, j'ai le pressetiment et une sorte d'obligation comme si j'étais dans un jeu... \n qui me fait dire que je dois vous le donner car il vous sera plus important...>> \n Vous récupérez le parchemrin et rentrez au lobby...")
    inventaire["Parchemrin de Tony Hawk"]=1
    lieu=chrantier

def chrantier():
    '''Arrivée sur le chrantier'''
    global lieu
    global parchemrins
    reponse=input("Vous arrivez à la maison d'un vieil homme nommé Daoine Antiel \n <<Vous voyez, j'ai tellement d'argent que c'est pas moi qui fait les travaux chez moi>> \n On est d'accord j'ai beaucoup d'argent ?")
    if reponse.lower()=='en effet':
        input("Daoine Antiel vous regarde avec de grands yeux <<Intriguant... Laissez moi aller chercher quelque chose>> \n Il revient avec un parchemrin, OUAIS TROP BIEN J'ADORE CA. \n  \n Vous obtenez le parchemrin de Daoine Antiel et sa thune et repartez en ville")
        inventaire['La thune du vieux']=1
        inventaire['Parchemrin de Daoine Antiel']=1
        lieu=lobby
    else :
        lieu=chrantier1

def chrantier1():
    '''Le vieux veut une baguette'''
    global lieu
    reponse=input("<<Bon, vous voulez pas répondre... Pour la peine vous pouvez aller me cherchezr une baguette pendant que je surveille leur bordel? \n Attendez moi, je vais chercher de l'argent>> \n Voulez vous : \n Attendre qu'il vous donne l'argent sagement : taper attendre\n Ou voulez vous l'espionner pour voir où il cache sa thune : tapez espionner \n Pour revenir au centre vrille, tapez vrille")
    if reponse=='espionner':
        lieu=Jardrin_thune
    elif reponse=='attendre':
        lieu=baguette
    elif reponse=='vrille':
        lieu=lobby

def Jardrin_thune():
    '''Le joueur découvre l'argent dans le jardrin'''
    global lieu
    input("Vous regardez alors que Daoine Antiel déterre avec un air déter-miné de l'argent dans son jardin. \n Plus précisément, il semble avoir enterré l'argent sous ses légumes \n Vous faites semblant de n'avoir rien vu")
    lieu=baguette

def baguette():
    '''Le joueur va chercher une baguette à la boulangrerie'''
    global lieu
    input("Le vieux vous donne l'argent et vous amène à son Jet privé pour un tout tout petit trajet \n (Privé le jet hein) \n Avant que vous n'ayez le temps de culpabilisé sur votre bilan carbone, vous arrivez à la boulangrerie \n Vous offrez un billet de 100 euros pour payer 1 euro et 35 centimes et revenait avec la baguette par le jet privé \n (toujours privé le jet) \n")
    lieu=maison

def maison():
    '''Entrée dans la maison du vieux'''
    global lieu
    reponse=input("Le vieux récupère la baguette et vous laisse entrer dans sa maison (j'avais la flemme de faire des dialogues) \n Voulez-vous : \n Regarder dans le salon : tapez salon \n Aller dans le jardrin : tapez jardrin \n Aller en ville : ville")
    if reponse=='salon':
        lieu=salon
    elif reponse=='jardrin':
        lieu=jardrin
    elif reponse=='ville':
        lieu=lobby

def maison_bis():
    '''Maison sans l'histoire (après que tu sois déja passé par la maison'''
    global lieu
    reponse=input("Voulez-vous : \n Regarder dans le salon : tapez salon \n Aller dans le jardrin : tapez jardrin \n Aller en ville : ville")
    if reponse=='salon':
        lieu=salon
    elif reponse=='jardrin':
        lieu=jardrin
    elif reponse=='ville':
        lieu=lobby

def jardrin():
    '''Dans le jardrin'''
    global lieu
    reponse=input("Vous vous dirigez dans le jardrin, et voyez que des légumes ne sont plus en très bonne santé \n Voulez-vous inspecter la terre : terre \n Ou voulez-vous revenir dans la maison : maison")
    if reponse=='maison':
        lieu=maison_bis
    elif reponse=='terre':
        lieu=deterre

def deterre():
    '''Obtention de l'argent du vieux'''
    global lieu
    global inventaire
    input("En investiguant sous la terre, vous trouvés des liasses de billets \n Ce vieux cachait de la thune dans son jardrin, ça fait 2 fois moins de places pour les légumes! \n Bref, vous plein de liasses de billets et recomblez le trou aavnt de revenir dans la maison")
    inventaire['La thune du vieux']=1
    lieu=maison_bis

def salon():
    '''Découverte du tableau'''
    global lieu
    reponse=input("En explorant le salon, vous tombez sur un tableau du vieux avec un homme qui vous est familier \n Ils semblent être au stud en train de produire un classique \n Le cadre a accumulé la poussière, il serait donc resté ici très longtemps. Voulez-vous prendre le cadre pour le nettoyer : cadre \n Ou explorer plus la maison : maison")
    if reponse=='maison':
        lieu=maison_bis
    elif reponse=='cadre':
        lieu=cadre

def cadre():
    '''Aquisition du parchemrin de Daoine Antiel'''
    global lieu
    global inventaire
    input("Vous déposéz la peinture entouré par le cadre délicatement sur la table, mais en regardant le cadre, vous trouvez quelque chose \n Il s'agit d'un des parchemrins de légende ! \n Vous récupérez le parchemrin et replacer le tableau avant de vous replacer à l'entrée de la maison comme si de rien n'était")
    inventaire['Parchemrin de Daoine Antiel']=1
    lieu=maison_bis

def dojro():
    '''Dans le dojro'''
    global lieu
    reponse=input("vous arrivez au dojro, berceau du légendraire maître de la légendre.\nSes diciples sont déjà en rang quand vous arrivez, comme s'il était au courrant que des visiteurs allais arriver.\nEn fait ils sont juste là pour leur demi heure de soleil journalière, le reste de la journée, ils préparent des singeries au stud.\nVisiblement, vous n'êtes pas les bienvenus, et leur temps de soleil est bientôt fini. Ils vont retourner cook, il faut agir vite !\nQue faire ?\n-attendre et les suivre dans leur antre\n-leur donner la thune du vieux")
    if reponse=="leur donner la thune du vieux" :
        if inventaire['La thune du vieux']==1 :
            lieu=CoeurDeLaMontagne
        else :
            input("Vous n'avez pas assez d'argent pour corrompre les disciples, alors vous retournez en ville.")
            lieu=lobby
    elif reponse=="attendre et les suivre dans leur antre":
        lieu=lore

def lore():
    '''Le joueur obtient le Lore'''
    global lieu
    global inventaire
    reponse=input("Nous sommes les diciples du maître qui a écrit \nune partie de la Légendre, en compagnie de Tony Hawk, du Grand Empereur, de Daoine Antiel et de la Nonne. \n Ils voulais créer un monde meilleur en répandant ces écrits a travers le pays d'Epatximacaciziz.\nLors de leur quêtes ils ont affronté bien des censures a leur oeuvre, \n mais au final c'est aujourd'hui grâce a elle que le monde est un endroit relativement sûr.\nLui et ces camarades ont affronté vlah les problèmes \n et ils ont pu ensuite se séparer car leur oeuvre était finie...\nCet homme, notre maître, il est ton père. \n \n Maintenant que vous comprenez ce qu'il s'est passé dans la ville de Levrille, voulez-vous y retourner : taper ville \n Ou voulez-vous donner de l'argent aux gardes pour qu'il vous amène voir votre père ? : taper argent")
    inventaire["lore"]=1
    if reponse=='argent':
        if inventaire['La thune du vieux']==1 :
            lieu=CoeurDeLaMontagne
        else :
            input("Vous n'avez pas assez d'argent pour corrompre les disciples, alors vous retournez en ville.")
            lieu=lobby
    elif reponse=='ville':
        lieu=lobby

def CoeurDeLaMontagne():
    '''Rencontre avec notre père'''
    global lieu
    reponse=input("Ils vous ont emmené au coeur de la montagne en jet (privé le jet), car quand même la thune c'est cool.\n Ils vous ont juste dit de vous méfier du vieil ermite qui vit là.\nIl est leur maître et est un combatant hors paire, qui s'est exilé en quête de rédemption...\nIls vous déposent devant un petit sentier qui semble mener au centre d'une grande clairière\n au beau milieu de la montagne, dont on dit qu'elle reste fleurie toute l'année.\nLorsque vous appercevez les premières fleurs, vous arrivez dans la valée. \nOn ne vous a pas menti, cette clairière est belle et bien pleine de fleurs, et vous appercevez un homme assis au milieu ce cratère.\nLe seul problème est qu'une pente comme celle que vous avez sous les pieds serai impossible a remonter une fois que vous serez dedans.\nVous déscendez et arrivez devant l'homme mysterieux, il n'est pas spécialement impressionant,\n mais ses élèves vous ont raconté tellement de choses que vous gardez une certaine distance...\nIl se retourne et vous adresse ces paroles: moitié diego + moitié diego, ça fait ?\n-ça fait 1 diego\n-t'as coupé un mec en deux ?\n-elle est nulle cette question, qui a écrit cette merde ?")
    if reponse=="ça fait 1 diego":
        input("Qui est tu ? Seuls mes déscendants peuvent connaitre la réponse a ce dilemme...")
        lieu=AllParchemrin
    elif reponse=="t'as coupé un mec en deux ?":
        input("Dommage, mais ce n'était pas la bonne réponse a sa question. Il vous traite de 'golmon' et vous explose la gueule, c'est game over...")
        lieu="perdu"
    elif reponse=="elle est nulle cette question, qui a écrit cette merde ?":
        input("tu mérite même pas de jouer")
        lieu="perdu"

def AllParchemrin():
    '''Fin du jeu ?'''
    global lieu
    global inventaire
    if inventaire["Parchemrin de Tony Hawk"]==1 and inventaire["Parchemrin de la Nonne"]==1 and inventaire["Parchemrin de Daoine Antiel"]==1 and inventaire["lore"]==1:
        input("Qui est-tu ? Tu n'est pas un simple voyageur... \n Donne moi les parchemrins que tu as réccupéré durant ton voyage, je vais te montrer a quoi ils servent réellement.\nVous lui donnez les parchemrins, et il se met a réciter des paroles dans une langue qui ne vous est pas familière,\n on dirait juste qu'il bourré mais bon.\nAlors qu'il ferme enfin sa gueule, les parchemrins se liquéfient pour laisser place a une espèce de slime dégueulasse, \n vraiment ça pue sa mère...\nIl dépose l'immonde mixture dans un saladier sur lequel vous pouvez lire les inscription 'Ikea'.\nDès lors que cette merde touche le bol, le mélange prend immédiatement une magnifique couleur dorée \n(ça pue toujours, une odeur a mi-chemin entre un zizi et du caca).\nIl laisse à tremper pendant 1 minute puis, on laisse reposer pendant 10 minutes \nce qui vous on mis dans une telle situation d'inconfort que le cringe ne vous atteint plus.\nEnfin il sort la bouse du bol, mais a la place de l'étron que vous vous attendiez a voir,\nressort un supperbe parchemrin, plus grand et presque plus aussi puant.\nVous pouveé y lire: c'est pas qu'une histoire de zizi, c'est aussi une histoire de caca...")
        lieu='gagné'
    else :
        input("Désolé, il semblerait que malgré votre lucidité hors-pair, vous ne soyez pas l'élu \nOu alors, vous n'avez peut être pas trouvé tous les parchemrins ? \n Dans tous les cas, vous devriez revenir en ville, cela vaut mieux pour vous comme pour moi \n Vous vous retournez comme pour partir mais vous vous souvenez que vous êtes coincés dans le cratère... Dommage...")
        lieu='perdu'

def clochrer():
    '''Entrée dans le clochrer'''
    global lieu
    reponse=input("Une grande église. Voilà ce qui se trouve sous vos yeux, et surtout bien au dessus de vos têtes.\nVous y pénetrez et êtes acceuillis par une Nonne, qui vous récite un poème:\n\nMes pensées voguent vers l'inconnu,\nInstants suspendus, sur ma chaise, je suis perdu.\nXérès de l'ergonomie, elle me berce,\nTrône silencieux où l'inspiration perce.\nAssis, je rêve d'évasion,\nParcourant des mondes, sans limitation.\nEntre le cuir et le métal, un voyage.\n\n- Après avoir entendu ces quelques belles paroles, vous êtes en capacité de trouver le mot magique qui m'empèche de vous\nlaisser passer. Alors, quel est ce mot:\n-'ZIZI'\n-'CACA'\n-'MIXTAPE'\n- ATTAQUERLANONNE")
    if reponse=="ZIZI":
        input("Mais n'importe quoi ptn.")
        lieu=poussé
    elif reponse=="CACA":
        input("frr tu force.")
        lieu=poussé
    elif reponse=="MIXTAPE":
        input("Excellent... suis moi.")
        lieu=énigme
    elif reponse=="ATTAQUERLANONNE":
        input("elle vous casse la gueule et vous traine de force en haut du clochrer.")
        lieu=poussé

def énigme():
    '''Enigme consonne'''
    global lieu
    reponse=input("- Dorénavant, tu ne peut plus reculer... Je vais t'inflinger une dernière interrogation.\nCite moi dans le mot 'Mixtape' les lettres qu'on sonne, et qui rythment l'harmonie de cette partie du langage.\nEst-ce :\n-'MXTP'\n-'ZZCC'")
    if reponse=="MXTP":
        input("Tu est perspicace, suis moi encore un peu plus loin...")
        lieu=cloche
    elif reponse=="ZZCC":
        input("Tu est dans l'abus.")
        lieu=poussé

def poussé():
    '''Game Over, la nonne pousse le joueur du clochrer'''
    global lieu
    input("Dommage, mais la nonne te pousse du haut du clochrer.")
    lieu="perdu"

def cloche():
    '''Parchemrin de la nonne'''
    global lieu
    global inventaire
    input("Toi qui a prouvé que tu est digne de le recevoir, obtient alors le Parchemrin de la Nonne")
    inventaire["Parchemrin de la Nonne"]=1
    lieu=lobby

#Programme principal en fait

inventaire={"Parchemrin de la Nonne":0,"Parchemrin de Tony Hawk":0,"Parchemrin de Daoine Antiel":0,"lore":0,"La thune du vieux":0}
lieu=histoire
while lieu not in ["gagné","perdu"] :
    lieu()
input("Vous avez "+lieu)