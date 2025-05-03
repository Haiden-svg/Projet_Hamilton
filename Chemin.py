from Graphe import *
from sommet import *
import random
class Chemin:
    def __init__(self): # Constructeur
        self.sommets = []
        self.poids = 0

    def ajouter_sommet(self, sommet): # Ajoute une sommet à la Chemin
        self.sommets.append(sommet) # Ajoute la sommet à la liste des sommets
        if len(self.sommets) >= 2: # Si la Chemin contient au moins 2 sommets
            self.poids += sommet.distance_vers(self.sommets[-2]) # Ajoute la distance entre la sommet et la précédente
        # Supprimez le retour à la sommet de départ pour Hamiltonian Path

    def ajouter_sommets(self, sommets): # Ajoute plusieurs sommets a la Chemin
        for sommet in sommets: # Pour chaque sommet dans la liste de sommets
            self.ajouter_sommet(sommet) # Ajoute la sommet a la Chemin

    def __str__(self): # Affiche la Chemin
        return f"Chemin: {self.sommets}, Poids: {self.poids}"     
    
    def mutate(self):
        # Choisissez deux indices aléatoires
        index1 = random.randint(0, len(self.sommets) - 1)
        index2 = random.randint(0, len(self.sommets) - 1)

        # Échangez les sommets à ces indices
        self.sommets[index1], self.sommets[index2] = self.sommets[index2], self.sommets[index1]

    def fitnessReload(self):
        self.poids = 0
        for i in range(len(self.sommets) - 1):  # S'arrête à l'avant-dernier élément
            self.poids += self.sommets[i].distance_vers(self.sommets[i+1]) # Ajoute la distance entre les sommets
        # Pas de boucle pour revenir à la sommet de départ