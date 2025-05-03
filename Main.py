import time
from Graphe import *
from Chemin import *
from Sommet import *
from Voyageur import *
from ListeChemin import *
from Grapics import *

class Main:
    france = Graphe(20) # Creez une Graphe
    # Creez un voyageur
    jean = Voyageur(france)
    list=ListeChemin()
    # Creez 100 Chemins
    for i in range(100):
        Chemin=Chemin()
        Chemin.ajouter_sommets(jean.voyager())
        Chemin.fitnessReload()
        list.add_Chemin(Chemin)

    # Début de la mesure du temps
    start_time = time.time()

    # Creez une fenetre graphique
    graphics = Graphics()
    graphics.draw_sommets(france.sommets, 'img/sommet.png')
    # Boucle d'évolution
    for generation in range(1000):  # Augmentez le nombre de générations
        list.evolutive_list_Chemin(2000)
        meilleure_Chemin = list.Chemins[0]
        if generation % 10 == 0: 
            graphics.update(meilleure_Chemin)

    # Fin de la mesure du temps
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")  # Affiche le temps d'exécution

    list.print_Chemins()
    graphics.show()
    # Affichez les chemins (Hamiltonian Path)
