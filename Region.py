from Ville import *
import random
class Region:
    def __len__(self):
        return len(self.villes) # Retourne le nombre de villes dans la region
    def __init__(self, number=None): # Constructeur
        self.villes = []
        if number is not None: # Si le nombre de villes est specifie
            for i in range(number): # Creez le nombre de villes specifie
                self.villes.append(Ville("Ville " + str(i), random.randint(0, 100), random.randint(0, 100))) # Creez une ville avec des coordonnees aleatoires
    
    def afficher_villes(self): # Affiche toutes les villes de la region
        for ville in self.villes: # Pour chaque ville dans la liste des villes
            print(ville)

    def ajouter_ville(self, ville): # Ajoute une ville a la region
        self.villes.append(ville)
    
    def ajouter_villes(self, villes): # Ajoute plusieurs villes a la region
        for ville in villes:
            self.ajouter_ville(ville)

    def enlever_ville(self, ville): # Enleve une ville de la region
        self.villes.remove(ville)

    def choisir_ville_aleatoire(self): # Choisit une ville aleatoire
        return random.choice(self.villes)