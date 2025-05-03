import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time
class Graphics:
    def __init__(self): # Constructeur
        self.fig, self.ax = plt.subplots()

    def draw_cities(self, cities): # Dessine les villes
        for city in cities: # Pour chaque ville dans la liste des villes
            self.ax.plot(city.x, city.y, 'ro')  # 'ro' signifie un point rouge

    def draw_route(self, route): # Dessine la route
        x = [city.x for city in route.villes] # Coordonnées x des villes
        y = [city.y for city in route.villes] # Coordonnées y des villes
        if len(route.villes) > 1: # Si la route contient au moins 2 villes
            x.append(route.villes[0].x) # Ajoute la coordonnée x de la première ville pour boucler
            y.append(route.villes[0].y) # Ajoute la coordonnée y de la première ville pour boucler
        self.ax.plot(x, y, 'b-')  # 'b-' signifie une ligne bleue

    def show(self):
        plt.show() # Affiche le graphique

    def update(self, route): # Met a jour le graphique
        self.ax.clear() # Efface le graphique
        self.draw_cities(route.villes) # Dessine les villes
        self.draw_route(route) # Dessine la route
        plt.draw()
        plt.pause(0.1)  # Pause pour permettre la mise à jour du graphique