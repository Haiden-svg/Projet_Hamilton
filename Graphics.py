import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time

class Graphics:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
    def draw_graphe(self, graphe, img_path=None):
        for sommet in graphe.sommets:
            self.ax.plot(sommet.x, sommet.y, 'ro')
        drawn_edges = set()
        for sommet in graphe.aretes:
            for voisin in graphe.aretes[sommet]:
                edge = tuple(sorted([id(sommet), id(voisin)]))
                if edge not in drawn_edges:
                    x = [sommet.x, voisin.x]
                    y = [sommet.y, voisin.y]
                    self.ax.plot(x, y, 'k-', linewidth=0.5)
                    drawn_edges.add(edge)
    def draw_chemin(self, chemin):
        x = [sommet.x for sommet in chemin.sommets]
        y = [sommet.y for sommet in chemin.sommets]
        self.ax.plot(x, y, 'b-', linewidth=2)
    def show(self):
        plt.show()
    def update(self, chemin, graphe):
        self.ax.clear()
        self.draw_graphe(graphe)
        self.draw_chemin(chemin)
        plt.draw()
        plt.pause(0.1)