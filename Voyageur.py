import random
from Graphe import *
from Sommet import *
from Chemin import *
class Voyageur:
    def __init__(self, Graphe):
        self.Graphe = Graphe

    def voyager(self):
        
        # Cree une liste pour stocker les Graphes visitees
        visited_Graphes = []
        
        # Cree une liste pour stocker le trajet
        Chemin = []
        
        # Tant que toutes les Graphes n'ont pas ete visitees
        while len(visited_Graphes) < len(self.Graphe):
            # Choisir une Graphe aleatoire
            random_sommet = self.Graphe.choisir_sommet_aleatoire()
            
            # Verifier si la Graphe a deja ete visitee
            if random_sommet not in visited_Graphes:
                # Ajouter la Graphe a la liste des Graphes visitees
                visited_Graphes.append(random_sommet)
                
                # Ajouter la Graphe a la liste du trajet
                Chemin.append(random_sommet)
        
        # Print the final Chemin
        #print(Chemin)
        return Chemin