from Region import *
from Route import *
from Ville import *
from Voyageur import *
from ListeRoute import *
from Graphics import *
class Main:
    france = Region(20) # Creez une region
    # Creez un voyageur
    jean = Voyageur(france)
    list=ListeRoute()
    # Creez 100 routes
    for i in range(100):
        route=Route()
        route.ajouter_villes(jean.voyager())
        route.fitnessReload()
        list.add_route(route)

   
   # Creez une fenetre graphique
    graphics = Graphics()
    graphics.draw_cities(france.villes)
    # Boucle d'évolution
    for generation in range(100):  # Augmentez le nombre de générations
        list.evolutive_list_route(2000)
        meilleure_route = list.routes[0]
        if generation % 10 == 0: 
            graphics.update(meilleure_route)

    list.print_routes()
    graphics.show()
    # Affichez les chemins

        # Comparaison avec un seuil
    seuil = 400  # Définir le seuil ici
    score_final = list.routes[0].poids
      # Supposons que fitness représente le score final
    if score_final < seuil:
        print("Oui")
    else:
        print("Non")

