from Graphe import *
import random

class Explorateur:
    def __init__(self, graphe):
        self.Graphe = graphe
    
    def parcourir(self, complet=False):
        visited_sommets = []
        chemin = []
        current_sommet = self.Graphe.choisir_sommet_aleatoire()
        chemin.append(current_sommet)
        visited_sommets.append(current_sommet)
        
        if complet:
            # Pour un graphe complet, générer une permutation aléatoire des sommets restants
            remaining_sommets = [s for s in self.Graphe.sommets if s not in visited_sommets]
            random.shuffle(remaining_sommets)
            chemin.extend(remaining_sommets)
            return chemin
        else:
            # Pour un graphe non complet, vérifier les voisins
            while len(visited_sommets) < len(self.Graphe):
                voisins = [s for s in self.Graphe.aretes[current_sommet] if s not in visited_sommets]
                if not voisins:
                    return None  # Aucun chemin hamiltonien possible
                current_sommet = random.choice(voisins)
                chemin.append(current_sommet)
                visited_sommets.append(current_sommet)
            return chemin