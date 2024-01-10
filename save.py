###tout ce qui est rapport avec les sauvegardes


class Save:

    #sauvegarde la partie
    def save_game(self,tableau_jeu,joueur_actuel): #sauvegarde la partie en cours dans sauvegarde.txt
            
            print("Dans quelle sauvegarde souhaitez vous enregistrer la partie ?")
            
            self.num_sauvegarde = input()
        
            with open("sauvegarde"+self.num_sauvegarde+".txt","w") as fichier:
                
                fichier.seek(0) #on place le curseur au début juste au cas où
                
                fichier.write(str(joueur_actuel)+"\n")
                for i in tableau_jeu:
                    for j in i:
                        fichier.write(str(j))
                    fichier.write("\n")#on retourne à la ligne dès qu'on a écrit une ligne du plateau

    #Fonction qui importe la sauvegarde que l'utilisateur choisit.
    #Elle renvoie le numéro du joueur qui doit jouer en premier ainsi que le
    #plateau de jeu de la partie sauvegardée.
    def load_save(self):
            
        importer_ou_non = -1
        while importer_ou_non != 0 and importer_ou_non != 1:
            
            print("\nSouhaitez-vous reprendre une partie sauvegardée ?\n"
                                        "Entrez 1 si oui et 0 sinon")
            
            try:
                importer_ou_non = int(input())
            except ValueError:
                print("La commande entrée est invalide.")
                continue
            
            if importer_ou_non == 1:
                
                self.num_sauvegarde = 0
                while self.num_sauvegarde == 0:                        
                
                    print("\nQuelle sauvegarde souhaitez-vous importer ?")
                
                    try :
                        self.num_sauvegarde = int(input())
                    except:
                        print("La commande entrée est invalide.")
                        continue
                
                    
                    with open("sauvegarde"+str(self.num_sauvegarde)+".txt","r") as fichier:
                                            
                        fichier.seek(0)
                        
                        self.joueur_actuel = int(fichier.read(1)) #la première ligne de la sauvegarde indique à quel joueur est le tour
                        self.tableau_jeu=[]
                        fichier.read(1)#on passe le \n
                        for i in range(0,6):
                            sous_liste=[]
                            for j in range(0,7):
                                sous_liste.append(int(fichier.read(1))) 
                            #on ajoute les valeurs de la j-ème ligne de la sauvegarde dans la j-ème ligne du tableau
                            fichier.read(1) #on passe le \n qui est à la fin de chaque ligne
                                
                            self.tableau_jeu.append(sous_liste)
                        return [self.joueur_actuel,self.tableau_jeu]
            
            elif importer_ou_non == 0:
                pass
            else: 
                print("La commande est invalide.")
