import random
from Region import *
from Ville import *
from Route import *
class Voyageur:
    def __init__(self, region):
        self.region = region

    def voyager(self):
        
        # Cree une liste pour stocker les regions visitees
        visited_regions = []
        
        # Cree une liste pour stocker le trajet
        route = []
        
        # Tant que toutes les regions n'ont pas ete visitees
        while len(visited_regions) < len(self.region):
            # Choisir une region aleatoire
            random_ville = self.region.choisir_ville_aleatoire()
            
            # Verifier si la region a deja ete visitee
            if random_ville not in visited_regions:
                # Ajouter la region a la liste des regions visitees
                visited_regions.append(random_ville)
                
                # Ajouter la region a la liste du trajet
                route.append(random_ville)
        
        # Ajoute la première ville à la fin pour former un cycle
        route.append(route[0])
        
        return route