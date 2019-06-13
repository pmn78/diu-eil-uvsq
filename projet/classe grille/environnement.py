from grille import Grille

class Voyageur:
    def __init__(self, couleur, trajet, grille):
        self.couleur = couleur
        self.trajet = trajet
        self.grille = grille
        
    def seDeplacer(self):
        """
        Stratégie de déplacement 'bidon'
        """
        (x, y) = self.grille.getPosition(self)
        self.grille.setPosition(self, (x + 1, y + 2))
    
class Obstacle:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille

class Porte:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille
        