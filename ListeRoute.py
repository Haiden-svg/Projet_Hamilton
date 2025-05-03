import random
import concurrent.futures
from Region import *
from Ville import *
from Route import *

class ListeRoute:

    def __init__(self): # Constructeur
        self.routes = []

    def crossover(self,route1, route2):
        # Choisissez un point d'index aléatoire
        index = random.randint(1, len(route1.villes) - 1)

        # Créez les premières moitiés des nouvelles routes
        new_route1_villes = route1.villes[:index]
        new_route2_villes = route2.villes[:index]

        # Ajoutez les villes manquantes à la fin des nouvelles routes
        new_route1_villes += [ville for ville in route2.villes if ville not in new_route1_villes]
        new_route2_villes += [ville for ville in route1.villes if ville not in new_route2_villes]

        # Créez les nouvelles routes
        new_route1 = Route()
        new_route1.ajouter_villes(new_route1_villes)
        new_route2 = Route()
        new_route2.ajouter_villes(new_route2_villes)

        if random.randint(0,1000)<10: # 10% de chance de mutation
            new_route1.mutate()
        if random.randint(0,1000)<10: # 10% de chance de mutation
            new_route2.mutate()
        new_route1.fitnessReload() # Recalcul du poids
        new_route2.fitnessReload() # Recalcul du poids
        return new_route1, new_route2 # Retourne les deux nouvelles routes
    
    def add_route(self, route):
        self.routes.append(route) # Ajoute une route à la liste

    def remove_route(self, route):
        self.routes.remove(route)

    def get_routes(self):
        return self.routes

    def clear_routes(self):
        self.routes = []

    def print_routes(self):
        print("====================================")
        for route in self.routes:
            
            print(route)
            print("====================================")

    def trier_routes(self):
        self.routes.sort(key=lambda x: x.poids)
    
    def evolutive_list_route(self, n=50):
        def process_crossover(i):
            parent1 = self.routes[i]
            parent2 = self.routes[i + 1]
            return self.crossover(parent1, parent2)

        max_pairs = min(n, len(self.routes) - 1)  # Ensure valid range
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(process_crossover, range(max_pairs)))

        for child1, child2 in results:
            self.add_route(child1)
            self.add_route(child2)

        self.trier_routes()
        self.routes = self.routes[:50]  # Ajusté pour Hamiltonian Path