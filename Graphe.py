from Sommet import *
import random

class Graphe:
    def __len__(self):
        return len(self.sommets)
    
    def __init__(self, number=None, complet=False, prob_connexion=0.3):
        self.sommets = []
        self.aretes = {}
        if number is not None:
            # Créer les sommets
            for i in range(number):
                self.sommets.append(Sommet("sommet " + str(i), random.randint(0, 100), random.randint(0, 100)))
                self.aretes[self.sommets[-1]] = []
            
            # Créer les arêtes
            if complet:
                # Graphe complet : connecter chaque sommet à tous les autres
                for sommet in self.sommets:
                    for autre_sommet in self.sommets:
                        if sommet != autre_sommet:
                            self.aretes[sommet].append(autre_sommet)
            else:
                # Graphe non complet : connecter avec une probabilité
                for sommet in self.sommets:
                    for autre_sommet in self.sommets:
                        if sommet != autre_sommet and random.random() < prob_connexion:
                            self.aretes[sommet].append(autre_sommet)
                            self.aretes[autre_sommet].append(sommet)  # Graphe non orienté
    
    def afficher_sommets(self):
        for sommet in self.sommets:
            print(sommet)
    
    def ajouter_sommet(self, sommet):
        self.sommets.append(sommet)
        self.aretes[sommet] = []
    
    def ajouter_sommets(self, sommets):
        for sommet in sommets:
            self.ajouter_sommet(sommet)
    
    def enlever_sommet(self, sommet):
        self.sommets.remove(sommet)
        del self.aretes[sommet]
        for s in self.aretes:
            if sommet in self.aretes[s]:
                self.aretes[s].remove(sommet)
    
    def choisir_sommet_aleatoire(self):
        return random.choice(self.sommets)