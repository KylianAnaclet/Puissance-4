# -*- coding: utf-8 -*-



from Mode_de_jeu import Mode



class Puissance4:

    def __init__(self):
        
        #couleurs
        self.rouge = "\033[1;31m"
        self.jaune = "\033[1;33m"
        self.bleu = "\033[1;34m"
        self.violet = "\033[1;35m"
        self.vert = "\033[1;32m"
        self.blanc = "\033[0m"
        
        #le premier élément de cette liste contient la couleur du joueur 1
        #et la deuxième celle du joueur 2
        self.couleurJ = [self.rouge,self.jaune]




    def menu(self):

            choix = 0

            while choix != 4:
                
                print("\n--------------------")
                print(" 1 - Joueur VS Joueur")   
                print(" 2 - Joueur VS Ordinateur")
                print(" 3 - Changer la couleur des pions")
                print(" 4 - >> Quitter <<")
            
                try :
                    choix = int(input("Choisissez votre mode de jeu \n"))
                except ValueError:
                    print("La commande entrée est invalide.")
                    continue

                if choix == 1:
                
                            Mode.jeu_1VS1(self.couleurJ)
                        
                elif choix == 2:
                    
                    choix2 = 0
                    while choix2<1 or choix2>4:
                        print("\n--------------------")
                        print(" 1 - Débutant")   
                        print(" 2 - Intermédiaire")
                        print(" 3 - Pro")
                        print(" 4 - Revenir au menu principal")
                    
                        try :
                            choix2 = int(input("Choisissez le niveau de difficulté de l'ordinateur\n"))
                        except ValueError:
                            print("La commande entrée est invalide.")
                            continue
                        if choix2 == 1:
                            Mode.ordinateur_debutant(self.couleurJ)
        
                        elif choix2 == 2:
                            Mode.ordinateur_intermediaire(self.couleurJ)
                        
                        elif choix2 == 3:
                            Mode.ordinateur_pro(self.couleurJ)
                        
                        elif choix2 == 4:
                            pass                   
                        else:
                            print("La commande entrée est invalide.")
                            
                elif choix == 3:
                    
                    choix3 = 0
                    
                    while choix3 != 3 :
                    
                        print("\n--------------------")
                        print(" 1 - Changer la couleur de pion du "+self.couleurJ[0]+"Joueur 1"+self.blanc)
                        print(" 2 - Changer la couleur de pion du "+self.couleurJ[1]+"Joueur 2"+self.blanc)
                        print(" 3 - Revenir au menu principal")
                    
                        try:
                            choix3 = int(input())
                        except ValueError:
                            print("La commande entrée est invalide.")
                            continue
                        
                        if choix3 == 1 or choix3 == 2:
                            self.changer_couleur(choix3)
                        
                        else:
                            print("La commande entrée est invalide.")
                
                elif choix == 4:
                    pass
                
                else:
                    print("La commande entrée est invalide.")
            

            
                    
     
    
    def changer_couleur(self,joueur):
        
        choix_c = 0
        
        while choix_c < 1 or choix_c > 6:
            
            print("\n--------------------")
            print(" 1 - "+self.rouge+"Rouge"+self.blanc)
            print(" 2 - "+self.jaune+"Jaune"+self.blanc)
            print(" 3 - "+self.bleu+"Bleu"+self.blanc)
            print(" 4 - "+self.violet+"Violet"+self.blanc)
            print(" 5 - "+self.vert+"Vert"+self.blanc)
            print(" 6 - Revenir en arrière")
            
            try:
                choix_c = int(input("\nChoisissez la couleur de jeton du Joueur "+str(joueur)))
            
            except ValueError:
                print("La commande entrée est invalide.")
                continue
            
            if choix_c == 1:
                self.couleurJ[joueur-1] = self.rouge
            elif choix_c == 2:
                self.couleurJ[joueur-1] = self.jaune
            elif choix_c == 3:
                self.couleurJ[joueur-1] = self.bleu
            elif choix_c == 4:
                self.couleurJ[joueur-1] = self.violet
            elif choix_c == 5:
                self.couleurJ[joueur-1] = self.vert
            elif choix_c == 6:
                pass
            else:
                print("La commande entrée est invalide.")
                
        
                
Mode = Mode()


Puissance4 = Puissance4()



Puissance4.menu()
        

