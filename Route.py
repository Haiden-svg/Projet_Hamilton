from Region import *
from Ville import *
import random
class Route:
    def __init__(self): # Constructeur
        self.villes = []
        self.poids = 0

    def ajouter_ville(self, ville): # Ajoute une ville à la route
        self.villes.append(ville) # Ajoute la ville à la liste des villes
        if len(self.villes) >= 2: # Si la route contient au moins 2 villes
            self.poids += ville.distance_vers(self.villes[-2]) # Ajoute la distance entre la ville et la précédente
        if len(self.villes) > 2: # Si la route contient plus de 2 villes
            self.poids += self.villes[-1].distance_vers(self.villes[0]) # Ajoute la distance pour boucler

    def ajouter_villes(self, villes): # Ajoute plusieurs villes a la route
        for ville in villes: # Pour chaque ville dans la liste de villes
            self.ajouter_ville(ville) # Ajoute la ville a la route

    def __str__(self): # Affiche la route
        return f"Route: {self.villes}, Poids: {self.poids}"     
    
    def mutate(self):
        # Choisissez deux indices aléatoires
        index1 = random.randint(0, len(self.villes) - 1)
        index2 = random.randint(0, len(self.villes) - 1)

        # Échangez les villes à ces indices
        self.villes[index1], self.villes[index2] = self.villes[index2], self.villes[index1]

    def fitnessReload(self):
        self.poids = 0
        for i in range(len(self.villes) - 1):  # S'arrête à l'avant-dernier élément
            self.poids += self.villes[i].distance_vers(self.villes[i+1]) # Ajoute la distance entre les villes
        if len(self.villes) > 1: # Ajoute la distance pour boucler
            self.poids += self.villes[-1].distance_vers(self.villes[0])