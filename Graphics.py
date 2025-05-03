import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time

class Graphics:
    def __init__(self):  # Constructeur
        self.fig, self.ax = plt.subplots()

    def draw_graphe(self, graphe, dessiner_aretes=True):  # Dessine les sommets et optionnellement les arêtes
        # Dessiner les sommets
        for sommet in graphe.sommets:
            self.ax.plot(sommet.x, sommet.y, 'ro')  # Points rouges pour les sommets

        # Dessiner les arêtes si demandé
        if dessiner_aretes:
            drawn_edges = set()  # Pour éviter de dessiner les arêtes en double (graphe non orienté)
            for sommet in graphe.aretes:
                for voisin in graphe.aretes[sommet]:
                    edge = tuple(sorted([id(sommet), id(voisin)]))  # Tri pour éviter les doublons
                    if edge not in drawn_edges:
                        x = [sommet.x, voisin.x]
                        y = [sommet.y, voisin.y]
                        self.ax.plot(x, y, 'k-', linewidth=0.5)  # Lignes noires pour les arêtes
                        drawn_edges.add(edge)

    def draw_chemin(self, chemin):  # Dessine le chemin hamiltonien
        x = [sommet.x for sommet in chemin.sommets]  # Coordonnées x des sommets
        y = [sommet.y for sommet in chemin.sommets]  # Coordonnées y des sommets
        self.ax.plot(x, y, 'b-', linewidth=2)  # Ligne bleue pour le chemin hamiltonien

    def show(self):
        plt.show()  # Affiche le graphique

    def update(self, chemin, graphe, dessiner_aretes=True):  # Met à jour le graphique
        self.ax.clear()  # Efface le graphique
        self.draw_graphe(graphe, dessiner_aretes=dessiner_aretes)  # Dessine les sommets et optionnellement les arêtes
        self.draw_chemin(chemin)  # Dessine le chemin hamiltonien
        plt.draw()
        plt.pause(0.1)  # Pause pour permettre la mise à jour du graphique