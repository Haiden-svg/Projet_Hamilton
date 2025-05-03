import random
import concurrent.futures
from Graphe import *
from Sommet import *
from Chemin import *

class ListeChemins:
    def __init__(self):  # Constructeur
        self.chemins = []

    def crossover(self, chemin1, chemin2, graphe):
        # Vérifier que les chemins parents sont valides
        if not chemin1.est_valide(graphe) or not chemin2.est_valide(graphe):
            return None, None

        # Choisir deux indices aléatoires pour la sous-séquence
        index1 = random.randint(1, len(chemin1.sommets) - 2)
        index2 = random.randint(index1 + 1, len(chemin1.sommets) - 1)

        # Créer les nouveaux chemins
        new_chemin1 = Chemin()
        new_chemin2 = Chemin()

        # Copier la sous-séquence du parent 1 pour new_chemin1
        new_chemin1_sommets = chemin1.sommets[index1:index2]
        # Copier la sous-séquence du parent 2 pour new_chemin2
        new_chemin2_sommets = chemin2.sommets[index1:index2]

        # Compléter new_chemin1 avec les sommets de chemin2
        remaining_sommets1 = [s for s in chemin2.sommets if s not in new_chemin1_sommets]
        new_chemin1_sommets = self._construire_chemin_valide(new_chemin1_sommets, remaining_sommets1, graphe)
        if new_chemin1_sommets is None:
            return None, None  # Crossover impossible

        # Compléter new_chemin2 avec les sommets de chemin1
        remaining_sommets2 = [s for s in chemin1.sommets if s not in new_chemin2_sommets]
        new_chemin2_sommets = self._construire_chemin_valide(new_chemin2_sommets, remaining_sommets2, graphe)
        if new_chemin2_sommets is None:
            return None, None  # Crossover impossible

        # Ajouter les sommets aux nouveaux chemins
        new_chemin1.ajouter_sommets(new_chemin1_sommets)
        new_chemin2.ajouter_sommets(new_chemin2_sommets)

        # Appliquer une mutation avec 10% de chance
        if random.randint(0, 1000) < 100:  # Augmenté à 10%
            self._mutate_valide(new_chemin1, graphe)
        if random.randint(0, 1000) < 100:  # Augmenté à 10%
            self._mutate_valide(new_chemin2, graphe)

        # Recalculer les longueurs
        new_chemin1.calculer_longueur()
        new_chemin2.calculer_longueur()

        return new_chemin1, new_chemin2

    def _construire_chemin_valide(self, sous_sequence, remaining_sommets, graphe):
        """Construit un chemin valide en complétant la sous-séquence avec les sommets restants."""
        result = sous_sequence[:]
        remaining = remaining_sommets[:]

        # Compléter avant la sous-séquence
        while len(result) < len(graphe.sommets) and remaining:
            last_sommet = result[0] if result else None
            voisins = [s for s in remaining if last_sommet is None or s in graphe.aretes[last_sommet]]
            if not voisins:
                return None  # Impossible de construire un chemin valide
            next_sommet = random.choice(voisins)
            result.insert(0, next_sommet)
            remaining.remove(next_sommet)

        # Compléter après la sous-séquence
        while remaining:
            last_sommet = result[-1]
            voisins = [s for s in remaining if last_sommet in graphe.aretes[s]]
            if not voisins:
                return None  # Impossible de construire un chemin valide
            next_sommet = random.choice(voisins)
            result.append(next_sommet)
            remaining.remove(next_sommet)

        return result

    def _mutate_valide(self, chemin, graphe):
        """Effectue une mutation valide en inversant une sous-séquence."""
        if len(chemin.sommets) < 3:
            return

        # Choisir une sous-séquence à inverser
        index1 = random.randint(0, len(chemin.sommets) - 2)
        index2 = random.randint(index1 + 1, len(chemin.sommets) - 1)

        # Inverser la sous-séquence
        chemin.sommets[index1:index2 + 1] = chemin.sommets[index1:index2 + 1][::-1]

        # Vérifier la validité
        if not chemin.est_valide(graphe):
            # Annuler la mutation si invalide
            chemin.sommets[index1:index2 + 1] = chemin.sommets[index1:index2 + 1][::-1]

    def ajouter_chemin(self, chemin):
        self.chemins.append(chemin)  # Ajoute un chemin à la liste

    def supprimer_chemin(self, chemin):
        self.chemins.remove(chemin)

    def get_chemins(self):
        return self.chemins

    def clear_chemins(self):
        self.chemins = []

    def afficher_chemins(self):
        print("====================================")
        for chemin in self.chemins:
            print(chemin)
            print("====================================")

    def trier_chemins(self):
        self.chemins.sort(key=lambda x: x.longueur)

    def evoluer_chemins(self, graphe, n=50):
        def process_crossover(i):
            parent1 = self.chemins[i]
            parent2 = self.chemins[i + 1]
            return self.crossover(parent1, parent2, graphe)

        max_pairs = min(n, len(self.chemins) - 1)  # Ensure valid range
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(process_crossover, range(max_pairs)))

        for child1, child2 in results:
            if child1 is not None and child1.est_valide(graphe):
                self.ajouter_chemin(child1)
            if child2 is not None and child2.est_valide(graphe):
                self.ajouter_chemin(child2)

        self.trier_chemins()
        self.chemins = self.chemins[:50]  # Conserver les 50 meilleurs