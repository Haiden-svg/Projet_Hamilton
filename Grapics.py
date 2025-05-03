import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time
class Graphics:
    def __init__(self): # Constructeur
        self.fig, self.ax = plt.subplots()

    def draw_sommets(self, sommets, img_path=None): # Dessine les sommets
        for city in sommets: # Pour chaque sommet dans la liste des sommets
            self.ax.plot(city.x, city.y, 'ro')  # 'ro' signifie un point rouge

    def draw_Chemin(self, Chemin): # Dessine la Chemin
        x = [city.x for city in Chemin.sommets] # Coordonnées x des sommets
        y = [city.y for city in Chemin.sommets] # Coordonnées y des sommets
        self.ax.plot(x, y, 'b-')  # 'b-' signifie une ligne bleue

    def show(self):
        plt.show() # Affiche le graphique

    def update(self, Chemin): # Met a jour le graphique
        self.ax.clear() # Efface le graphique
        self.draw_sommets(Chemin.sommets, 'img/sommet.png') # Dessine les sommets
        self.draw_Chemin(Chemin) # Dessine la Chemin
        plt.draw()
        plt.pause(0.1)  # Pause pour permettre la mise à jour du graphique