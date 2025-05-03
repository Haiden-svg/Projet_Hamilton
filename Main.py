from Graphe import *
from Chemin import *
from Sommet import *
from Explorateur import *
from ListeChemins import *
from Graphics import *

class Main:
    # Demander à l'utilisateur le type de graphe
    while True:
        choix = input("Voulez-vous un graphe complet (c) ou non complet (n) ? [c/n] : ").lower()
        if choix in ['c', 'n']:
            complet = (choix == 'c')
            break
        print("Veuillez entrer 'c' pour complet ou 'n' pour non complet.")

    # Créer un graphe avec 40 sommets
    graphe = Graphe(20, complet=complet, prob_connexion=0.3)
    print(f"Graphe créé : {'complet' if complet else 'non complet (probabilité de connexion = 0.3)'}")

    # Créer un explorateur
    explorateur = Explorateur(graphe)
    liste_chemins = ListeChemins()

    # Créer 100 chemins valides
    attempts = 0
    max_attempts = 1000  # Limite pour éviter une boucle infinie
    while len(liste_chemins.get_chemins()) < 100 and attempts < max_attempts:
        chemin = Chemin()
        chemin_sommets = explorateur.parcourir(complet=complet)  # Passer le paramètre complet
        if chemin_sommets is not None:  # Vérifier si un chemin a été généré
            chemin.ajouter_sommets(chemin_sommets)
            if chemin.est_valide(graphe):  # Vérifier la validité
                chemin.calculer_longueur()
                liste_chemins.ajouter_chemin(chemin)
        attempts += 1

    if len(liste_chemins.get_chemins()) < 100:
        print(f"Attention : Seulement {len(liste_chemins.get_chemins())} chemins valides générés après {max_attempts} tentatives.")

    # Créer une fenêtre graphique
    graphics = Graphics()
    graphics.draw_graphe(graphe, dessiner_aretes=not complet) 

    # Boucle d'évolution
    for generation in range(1000):
        liste_chemins.evoluer_chemins(graphe, 2000)  # Passer le graphe
        if liste_chemins.get_chemins():  # Vérifier qu'il y a des chemins
            meilleur_chemin = liste_chemins.chemins[0]
            if generation % 10 == 0:
                graphics.update(meilleur_chemin, graphe, dessiner_aretes=not complet) 
        else:
            print(f"Génération {generation} : Aucun chemin valide. Arrêt.")
            break

    # Afficher uniquement le meilleur chemin
    if liste_chemins.get_chemins():
        print("====================================")
        print("Meilleur chemin hamiltonien trouvé :")
        print(liste_chemins.chemins[0])
        print("====================================")
    else:
        print("Aucun chemin hamiltonien valide trouvé.")

    graphics.show()