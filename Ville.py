class Ville:
    def __init__(self, nom, x, y): # Constructeur
        self.nom = nom
        self.x = x
        self.y = y

    def __str__(self): # Affiche la ville
        return f"Ville: {self.nom}, Coordonnées: ({self.x}, {self.y})"
    
    def __repr__(self): # Affiche la ville
        return self.__str__()

    def distance_vers(self, autre_ville): # Calcule la distance entre deux villes
        distance_x = abs(self.x - autre_ville.x) # Calcule la distance en x
        distance_y = abs(self.y - autre_ville.y) # Calcule la distance en y
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5   # Calcule la distance totale
        return distance
    
