from save import Save
from test_victoire import Victoire
import random
from random import randint


class Mode:
     
    def __init__(self):
        
        self.blanc = "\033[0m"
        
#####################################################################################
#les 4 modes de jeu (joueur contre joueur et jouer contre ordi avec les trois
#difficultés)    
    
    
    def jeu_1VS1(self,couleurJ):
            
            ##on crée (ou importe) le plateau de jeu
            
            self.game_over = False
            
            self.infos_partie_sauvegardee = save.load_save()

            #si load_save ne retourne rien c'est que l'utilisateur n'a pas importé de sauvegarde
            #donc on initalise le plateau de jeu
            if self.infos_partie_sauvegardee == None:
                self.init_plateau()   
                self.joueur_actuel = 1
            
            else:
                self.tableau_jeu = self.infos_partie_sauvegardee[1]
                self.joueur_actuel = self.infos_partie_sauvegardee[0]

            
            ##la partie commence

            while not self.tableau_plein() and not self.game_over :
                
                self.jouer_coup(self.joueur_actuel,couleurJ)
                
                #si game_over est déjà True parce que les joueurs souhaitent quitter la partie
                #alors il doit rester True, d'où le "or"
                self.game_over = victoire.test_gagnant(self.tableau_jeu) or self.game_over
            
            
            ##la partie est terminée
            
            if victoire.vainqueur != 0:
                self.afficher_plateau(couleurJ)
                print("Puissance 4 ! Le "+couleurJ[victoire.vainqueur-1]+"Joueur "+str(victoire.vainqueur)+self.blanc+" a gagné.")
            
            elif self.tableau_plein():
                self.afficher_plateau(couleurJ)
                print("Match nul ! Le plateau est rempli.")
            
    
    
    
    def ordinateur_pro(self,couleurJ):
       
        ##on crée (ou importe) le plateau
        
        self.game_over = False
        
        self.infos_partie_sauvegardee = save.load_save()
        

        if self.infos_partie_sauvegardee == None: 
            self.init_plateau()   
            self.joueur_actuel = 1
       
        else:
            self.tableau_jeu = self.infos_partie_sauvegardee[1]
            self.joueur_actuel = self.infos_partie_sauvegardee[0]
          
        
        ##la partie commence
        
        while not self.tableau_plein() and not self.game_over:
            
            if self.joueur_actuel == 1:
                self.jouer_coup(1,couleurJ)
                           
            else : 
                
                col = 0                
                    
                #le bot teste tous les coups possibles (chaque colonne)
                for i in range (0,7):
                    
                    #on check d'abord que la colonne n'est pas remplie.
                    #(Si c'est le cas on passe direct à la suivante)
                    if self.tableau_jeu[0][i] == 0:
                        
                        #le bot place son pion temporairement dans cette colonne
                        for ligne in range(5,-1,-1):   
                            if self.tableau_jeu[ligne][i] == 0:
                                self.tableau_jeu[ligne][i] = 2
                                #il garde en tete la ligne où il vient de jouer
                                ligne_pion = ligne
                                
                                break
                        
                        #une fois qu'il a placé son pion il teste avec la 
                        #fonction test_gagnant si il y a puissance 4
                        if victoire.test_gagnant(self.tableau_jeu) == True:
                            
                            #si oui il doit jouer ce coup puisqu'il le fait
                            #gagner.
                            col = i+1
                            
                            #il enlève le pion placé temporairement
                            self.tableau_jeu[ligne_pion][i] = 0
                            
                            #Comme gagner est prioritaire sur bloquer il
                            #peut déjà sortir de la boucle
                            break
                        
                        #cette fois il place temporairement le pion de 
                        #l'adversaire au lieu du sien
                        self.tableau_jeu[ligne_pion][i] = 1
                        
                        if victoire.test_gagnant(self.tableau_jeu) == True:
                            
                            #si il y a puissance 4 le bot doit bloquer,
                            #c'est-à-dire jouer ce coup pour éviter que son
                            #adversaire le fasse au prochain tour.
                            col = i+1
                        
                        #il enlève le pion placé temporairement
                        self.tableau_jeu[ligne_pion][i] = 0
                

                #si le bot n'a pas détecté de possiblité de puissance 4 pour lui
                #ou son adversaire, alors il joue au hasard
                if col == 0:
                    
                    col = randint(1,7)
                    
                    while self.tableau_jeu[0][col-1] != 0:
                        col = randint(1,7)
                
                #finalement il place son pion (pour de vrai)
                for ligne in range(5,-1,-1):   
                    if self.tableau_jeu[ligne][col-1] == 0:
                        self.tableau_jeu[ligne][col-1] = 2
                        
                        break
                
                self.changement_joueur()
                                
            self.game_over = victoire.test_gagnant(self.tableau_jeu) or self.game_over 
        
        
        ##la partie est terminée
        
        if victoire.vainqueur != 0:
            self.afficher_plateau(couleurJ)
            print("Puissance 4 ! Le "+couleurJ[victoire.vainqueur-1]+"Joueur "+str(victoire.vainqueur)+self.blanc+" a gagné.")
        
        elif self.tableau_plein():
            self.afficher_plateau(couleurJ)
            print("Match nul ! Le plateau est rempli.")




    def ordinateur_intermediaire(self,couleurJ):
        
        ##on crée (ou importe) le plateau
        
        self.game_over = False
        
        self.infos_partie_sauvegardee = save.load_save()
        

        if self.infos_partie_sauvegardee == None: 
            self.init_plateau()   
            self.joueur_actuel = 1
       
        else:
            self.tableau_jeu = self.infos_partie_sauvegardee[1]
            self.joueur_actuel = self.infos_partie_sauvegardee[0]
            
        ##la partie commence
        
        while not self.tableau_plein() and not self.game_over:
            
            if self.joueur_actuel == 1:
                self.jouer_coup(1,couleurJ)
                           
            else : 
                
                
                col = 0                
                 
                #le bot teste tous les coups possibles (chaque colonne)
                for i in range (0,7):
                    
                    #on check d'abord que la colonne n'est pas remplie.
                    #(Si c'est le cas on passe direct à la suivante)
                    if self.tableau_jeu[0][i] == 0:
                        
                        #le bot place le pion de son adversaire temporairement 
                        #dans cette colonne
                        for ligne in range(5,-1,-1):   
                            if self.tableau_jeu[ligne][i] == 0:
                                self.tableau_jeu[ligne][i] = 1
                                #il garde en tete la ligne où il vient de jouer
                                ligne_pion = ligne
                                
                                break
                        
                        
                        if victoire.test_gagnant(self.tableau_jeu) == True:
                            
                            
                            #si il y a puissance 4 le bot doit bloquer,
                            #c'est-à-dire jouer ce coup pour éviter que son
                            #adversaire le fasse au prochain tour.
                            col = i+1
                        
                        #il enlève le pion placé temporairement
                        self.tableau_jeu[ligne_pion][i] = 0
                

                #si le bot n'a pas détecté de possiblité de puissance 4 pour 
                #son adversaire, alors il joue au hasard
                if col == 0:
                                
                    col = randint(1,7)
                                
                    while self.tableau_jeu[0][col-1] != 0:
                        col = randint(1,7)
                
                #finalement il place son pion (pour de vrai)
                for ligne in range(5,-1,-1):   
                    if self.tableau_jeu[ligne][col-1] == 0:
                        self.tableau_jeu[ligne][col-1] = 2
                        
                        break
                
                self.changement_joueur()
                                
            self.game_over = victoire.test_gagnant(self.tableau_jeu) or self.game_over 
        
        
        ##la partie est terminée
        
        if victoire.vainqueur != 0:
            self.afficher_plateau(couleurJ)
            print("Puissance 4 ! Le "+couleurJ[victoire.vainqueur-1]+"Joueur "+str(victoire.vainqueur)+self.blanc+" a gagné.")
        
        elif self.tableau_plein():
            self.afficher_plateau(couleurJ)
            print("Match nul ! Le plateau est rempli.")
    


    def ordinateur_debutant(self,couleurJ):
        
        ##on crée (ou importe) le plateau
        
        self.game_over = False
        
        self.infos_partie_sauvegardee = save.load_save()
        

        if self.infos_partie_sauvegardee == None: 
            self.init_plateau()   
            self.joueur_actuel = 1
       
        else:
            self.tableau_jeu = self.infos_partie_sauvegardee[1]
            self.joueur_actuel = self.infos_partie_sauvegardee[0]
            
        ##la partie commence
        
        while not self.tableau_plein() and not self.game_over:
            
            if self.joueur_actuel == 1:
                self.jouer_coup(1,couleurJ)
                           
            else : 
                
                nb_aleatoire = random.random() # nb aléatoire entre 0 et 1
                proba = 0.5 # 50% 
                col = 0                
                print(nb_aleatoire)   
                #le bot teste tous les coups possibles (chaque colonne)
                for i in range (0,7):
                    
                    #on check d'abord que la colonne n'est pas remplie.
                    #(Si c'est le cas on passe direct à la suivante)
                    if self.tableau_jeu[0][i] == 0:
                        
                        #le bot place le pion de son adversaire temporairement dans cette colonne
                        for ligne in range(5,-1,-1):   
                            if self.tableau_jeu[ligne][i] == 0:
                                self.tableau_jeu[ligne][i] = 1
                                #il garde en tete la ligne où il vient de jouer
                                ligne_pion = ligne
                                
                                break

                        #le bot bloque le puissance 4 de l'adversaire 1 fois sur 2
                        if victoire.test_gagnant(self.tableau_jeu) == True and nb_aleatoire < proba:
                            
                            col = i+1
                        
                        #il enlève le pion placé temporairement
                        self.tableau_jeu[ligne_pion][i] = 0
                

                
                #s'il n'a pas détecté de puissance 4 et ou proba pas respectée, alors il joue au hasard
                if col == 0:
                                
                    col = randint(1,7)
                                
                    while self.tableau_jeu[0][col-1] != 0:
                        col = randint(1,7)
                
                #finalement il place son pion (pour de vrai)
                for ligne in range(5,-1,-1):   
                    if self.tableau_jeu[ligne][col-1] == 0:
                        self.tableau_jeu[ligne][col-1] = 2
                        
                        break
                
                self.changement_joueur()
                                
            self.game_over = victoire.test_gagnant(self.tableau_jeu) or self.game_over 
        
        
        ##la partie est terminée
        
        if victoire.vainqueur != 0:
            self.afficher_plateau(couleurJ)
            print("Puissance 4 ! Le "+couleurJ[victoire.vainqueur-1]+"Joueur "+str(victoire.vainqueur)+self.blanc+" a gagné.")
        
        elif self.tableau_plein():
            self.afficher_plateau(couleurJ)
            print("Match nul ! Le plateau est rempli.")
    


######################################################################################
#sous-programmes qui permettent au jeu de bien fonctionner

    
    #demande au joueur où il souhaite placer son pion, puis le place
    def jouer_coup(self,joueur,couleurJ):
        
        col = 0
        
        while col < 1 or col > 7:
            
            print("Au tour du "+couleurJ[joueur-1]+"Joueur "+str(joueur)+self.blanc+" !\n")
            self.afficher_plateau(couleurJ)
            print("Choisissez une colonne (1, 7) ou entrez 0 pour mettre en pause")
            
            try:
                col = int(input())
            except ValueError:
                print("La commande entrée est invalide.")
                continue
            
            if col == 0:
                self.pause()
                break
            
            # check si colonne entrée est valide et si elle n'est pas déjà remplie
            elif 1 <= col <= 7 and self.tableau_jeu[0][col-1] == 0:
                
                for ligne in range (5, -1, -1): # test chaque ligne si la colonne est vide en partant du bas
                        if self.tableau_jeu[ligne][col-1] == 0:
                            self.tableau_jeu[ligne][col-1] = joueur # placement du pion ( 1 ou 2) en fonction du joueur
                            
                            break
                
                self.changement_joueur() #on change de joueur seulement si un coup a bien été joué
                
            else:
                print("Colonne invalide")


    
#vérifie si le plateau de jeu est plein
    def tableau_plein(self):

        tab_plein = True
        for i in self.tableau_jeu[0]: #on regarde uniquement la ligne du haut du tableau...            
            if i == 0: #...si elle contient au moins un 0 alors elle n'est pas pleine
                tab_plein=False
                break        
                
        return tab_plein
    
    #initialise le plateau de jeu (crée une matrice 6x7 avec que des 0)
    def init_plateau(self):

        self.tableau_jeu = []
        
        for i in range (0,6): # matrice de 6 lignes...
            sous_liste=[]
            for j in range (0,7): #...et 7 colonnes...
                sous_liste.append(0) #...remplie de 0
            self.tableau_jeu.append(sous_liste)
        

    def afficher_plateau(self,couleurJ): 
        
        for i in self.tableau_jeu:
            ligne=""
            for j in i:
                #si il n'y a pas de jeton on affiche juste 0
                if j == 0:
                    ligne += "0 "
                #si il y en a un on affiche un O de la couleur du joueur
                else:
                    ligne += couleurJ[j-1]+"O "+self.blanc 
            print("                         "+ligne)
        print("\n")

                
    
    def changement_joueur(self):
         
         if self.joueur_actuel == 2:
            self.joueur_actuel = 1
         else: 
            self.joueur_actuel = 2


    #menu qui s'affiche quand on met une partie en pause
    def pause(self):
        print("\n----- Le jeu est en pause -----")
        choix = 0
        
        while choix <1 or choix>3:
            print(" 1 - Reprendre la partie")
            print(" 2 - Quitter sans sauvegarder la partie")
            print(" 3 - Quitter et sauvegarder la partie")
            
            try: 
                choix = int(input())
            except ValueError:
                print("La commande entrée est invalide.\n")
                continue
            
            if choix == 1:
                pass
            
            elif choix == 2:
                self.game_over = True
            
            elif choix == 3:
                save.save_game(self.tableau_jeu,self.joueur_actuel)
                self.game_over = True
            
            else:
                print("La commande est invalide.\n")
                
    
 

                


save = Save()
victoire = Victoire()