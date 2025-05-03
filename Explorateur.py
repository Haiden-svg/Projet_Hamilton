import random
from Graphe import *
from Sommet import *
from Chemin import *

class Explorateur:
    def __init__(self, Graphe):
        self.Graphe = Graphe

    def parcourir(self):
        visited_sommets = []
        chemin = []
        current_sommet = self.Graphe.choisir_sommet_aleatoire()
        chemin.append(current_sommet)
        visited_sommets.append(current_sommet)
    
        while len(visited_sommets) < len(self.Graphe):
            voisins = [s for s in self.Graphe.aretes[current_sommet] if s not in visited_sommets]
            if not voisins:  # Pas de voisin non visité
                return None  # Aucun chemin hamiltonien possible
            current_sommet = random.choice(voisins)
            chemin.append(current_sommet)
            visited_sommets.append(current_sommet)
    
        return chemin