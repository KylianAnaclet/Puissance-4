
class Victoire:

    #check si il y a un puissance 4 dans le tableau de jeu mis en entrée
    #renvoie True si oui et False sinon    
    def test_gagnant(self,tableau_jeu):
            
            self.vainqueur = 0
            self.game_over = False
            

            ## victoire horizontale
            
            #joueur 1            
            for ligne in range(6):
                for col in range(7-3): # (7-3) pour rester dans la taille de 7 colonnes
                    if (tableau_jeu[ligne][col] == 1 and 
                        tableau_jeu[ligne][col+1] == 1  and 
                        tableau_jeu[ligne][col+2] == 1 and 
                        tableau_jeu[ligne][col+3] == 1):
                        
                        self.vainqueur = 1
                        self.game_over = True
        
                        break
                    
                    if (tableau_jeu[ligne][col] == 2 and 
                    tableau_jeu[ligne][col+1] == 2  and 
                    tableau_jeu[ligne][col+2] == 2 and 
                    tableau_jeu[ligne][col+3] == 2):
                        
                        self.vainqueur = 2
                        self.game_over = True
                        
                        break
        
            # victoire verticale
            
            for col in range(7):
                for ligne in range(6-3):
                    #Joueur 1
                    if (tableau_jeu[ligne][col] == 1 and 
                    tableau_jeu[ligne+1][col] == 1 and 
                    tableau_jeu[ligne+2][col] == 1 and 
                    tableau_jeu[ligne+3][col] == 1):
                        
                        self.vainqueur = 1
                        self.game_over = True
                        
                        break              
                    
                    #Joueur 2
                    if (tableau_jeu[ligne][col] == 2 and 
                    tableau_jeu[ligne+1][col] == 2 and 
                    tableau_jeu[ligne+2][col] == 2 and 
                    tableau_jeu[ligne+3][col] == 2):
                        
                        self.vainqueur = 2
                        self.game_over = True 
                        
                        break              
            
            
            # victoire diagonale
            
            #Joueur 1
            for ligne in range(6 - 3): #vers le bas (rappel : la ligne 0 est la ligne du haut)
                for col in range(7 - 3):
                    if (tableau_jeu[ligne][col] == 1 and
                        tableau_jeu[ligne + 1][col + 1] == 1 and
                        tableau_jeu[ligne + 2][col + 2] == 1 and
                        tableau_jeu[ligne + 3][col + 3] == 1):
                        
                        self.vainqueur = 1
                        self.game_over = True
                        
                        break

            for ligne in range(3, 6): #vers le haut
                for col in range(7 - 3):
                    if (tableau_jeu[ligne][col] == 1 and
                        tableau_jeu[ligne - 1][col + 1] == 1 and
                        tableau_jeu[ligne - 2][col + 2] == 1 and
                        tableau_jeu[ligne - 3][col + 3] == 1):
                        
                        self.vainqueur = 1
                        self.game_over = True
                        
                        break

            #Joueur 2
            for ligne in range(6 - 3): #vers le bas
                for col in range(7 - 3):
                    if (tableau_jeu[ligne][col] == 2 and
                        tableau_jeu[ligne + 1][col + 1] == 2 and
                        tableau_jeu[ligne + 2][col + 2] == 2 and
                        tableau_jeu[ligne + 3][col + 3] == 2):
                        
                        self.vainqueur = 2
                        self.game_over = True
                    
                        break

            for ligne in range(3, 6): #vers le haut
                for col in range(7 - 3):
                    if (tableau_jeu[ligne][col] == 2 and
                        tableau_jeu[ligne - 1][col + 1] == 2 and
                        tableau_jeu[ligne - 2][col + 2] == 2 and
                        tableau_jeu[ligne - 3][col + 3] == 2):
                        
                        self.vainqueur = 2
                        self.game_over = True
                        
                        break
                    
        
            return self.game_over