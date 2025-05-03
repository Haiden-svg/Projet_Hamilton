from Sommet import *
import random
class Graphe:
    def __len__(self):
        return len(self.sommets) # Retourne le nombre de sommets dans la Graphe
    def __init__(self, number=None): # Constructeur
        self.sommets = []
        if number is not None: # Si le nombre de sommets est specifie
            for i in range(number): # Creez le nombre de sommets specifie
                self.sommets.append(Sommet("sommet " + str(i), random.randint(0, 100), random.randint(0, 100))) # Creez une sommet avec des coordonnees aleatoires
    
    def afficher_sommets(self): # Affiche toutes les sommets de la Graphe
        for sommet in self.sommets: # Pour chaque sommet dans la liste des sommets
            print(sommet)

    def ajouter_sommet(self, sommet): # Ajoute une sommet a la Graphe
        self.sommets.append(sommet)
    
    def ajouter_sommets(self, sommets): # Ajoute plusieurs sommets a la Graphe
        for sommet in sommets:
            self.ajouter_sommet(sommet)

    def enlever_sommet(self, sommet): # Enleve une sommet de la Graphe
        self.sommets.remove(sommet)

    def choisir_sommet_aleatoire(self): # Choisit une sommet aleatoire
        return random.choice(self.sommets)