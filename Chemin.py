from Graphe import *
from Sommet import *
import random

class Chemin:
    def __init__(self):  # Constructeur
        self.sommets = []
        self.longueur = 0

    def ajouter_sommet(self, sommet):  # Ajoute un sommet au chemin
        self.sommets.append(sommet)  # Ajoute le sommet à la liste des sommets
        if len(self.sommets) >= 2:  # Si le chemin contient au moins 2 sommets
            self.longueur += sommet.distance_vers(self.sommets[-2])  # Ajoute la distance entre le sommet et le précédent
        

    def ajouter_sommets(self, sommets):  # Ajoute plusieurs sommets au chemin
        for sommet in sommets:  # Pour chaque sommet dans la liste de sommets
            self.ajouter_sommet(sommet)  # Ajoute la sommet au chemin

    def __str__(self):  # Affiche le chemin
        return f"Chemin: {self.sommets}, Longueur: {self.longueur}"     
    
    def mutate(self):
        # Choisissez deux indices aléatoires
        index1 = random.randint(0, len(self.sommets) - 1)
        index2 = random.randint(0, len(self.sommets) - 1)

        # Échangez les sommets à ces indices
        self.sommets[index1], self.sommets[index2] = self.sommets[index2], self.sommets[index1]

    def calculer_longueur(self):
        self.longueur = 0
        for i in range(len(self.sommets) - 1):  # S'arrête à l'avant-dernier élément
            self.longueur += self.sommets[i].distance_vers(self.sommets[i+1])  # Ajoute la distance entre les sommets
        # Pas de boucle pour revenir à la sommet de départ
    
    def est_valide(self, graphe):
        if len(self.sommets) != len(graphe):
            return False
        if len(set(self.sommets)) != len(self.sommets):
            return False
        for i in range(len(self.sommets) - 1):
            if self.sommets[i+1] not in graphe.aretes[self.sommets[i]]:
                return False
        return True