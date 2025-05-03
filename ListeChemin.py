import random
import concurrent.futures
from Graphe import *
from sommet import *
from Chemin import *

class ListeChemin:

    def __init__(self): # Constructeur
        self.Chemins = []

    def crossover(self,Chemin1, Chemin2):
        # Choisissez un point d'index aléatoire
        index = random.randint(1, len(Chemin1.sommets) - 1)

        # Créez les premières moitiés des nouvelles Chemins
        new_Chemin1_sommets = Chemin1.sommets[:index]
        new_Chemin2_sommets = Chemin2.sommets[:index]

        # Ajoutez les sommets manquantes à la fin des nouvelles Chemins
        new_Chemin1_sommets += [sommet for sommet in Chemin2.sommets if sommet not in new_Chemin1_sommets]
        new_Chemin2_sommets += [sommet for sommet in Chemin1.sommets if sommet not in new_Chemin2_sommets]

        # Créez les nouvelles Chemins
        new_Chemin1 = Chemin()
        new_Chemin1.ajouter_sommets(new_Chemin1_sommets)
        new_Chemin2 = Chemin()
        new_Chemin2.ajouter_sommets(new_Chemin2_sommets)

        if random.randint(0,1000)<10: # 10% de chance de mutation
            new_Chemin1.mutate()
        if random.randint(0,1000)<10: # 10% de chance de mutation
            new_Chemin2.mutate()
        new_Chemin1.fitnessReload() # Recalcul du poids
        new_Chemin2.fitnessReload() # Recalcul du poids
        return new_Chemin1, new_Chemin2 # Retourne les deux nouvelles Chemins
    
    def add_Chemin(self, Chemin):
        self.Chemins.append(Chemin) # Ajoute une Chemin à la liste

    def remove_Chemin(self, Chemin):
        self.Chemins.remove(Chemin)

    def get_Chemins(self):
        return self.Chemins

    def clear_Chemins(self):
        self.Chemins = []

    def print_Chemins(self):
        print("====================================")
        for Chemin in self.Chemins:
            
            print(Chemin)
            print("====================================")

    def trier_Chemins(self):
        self.Chemins.sort(key=lambda x: x.poids)
    
    def evolutive_list_Chemin(self, n=50):
        max_pairs = min(n, len(self.Chemins) - 1)  # Ensure valid range
        results = []
        for i in range(max_pairs):  # Boucle séquentielle
            parent1 = self.Chemins[i]
            parent2 = self.Chemins[i + 1]
            results.append(self.crossover(parent1, parent2))

        for child1, child2 in results:
            self.add_Chemin(child1)
            self.add_Chemin(child2)

        self.trier_Chemins()
        self.Chemins = self.Chemins[:50]  # Ajusté pour Hamiltonian Path