class Carte:
    """ Definit le plan dans lequel vont se deplacer les voygeurs"""
    def __init__(self,dimensions,portes,obstacles):
        self.dimensions=dimensions
        self.portes=portes
        self.obstacles=obstacles


class Case:
    """ Definit une case de la carte. Deux etats : occupee ou non occupee """
    def __init__(self,etat):
        self.occupee=etat
        self.cases_accessibles=[]

    def set_cases_accessibles(self,listeCases):
        # Determine la liste des cases accessibles d'une case donnee
        self.cases_accessibles=listeCases
        
        

class Voyageur:
    """ Definit un voyageur se deplacant sur la carte ; il doit savoir
    ou il va. S'il  rencontre un obstacle il doit le contourner (pas de
    deplacement en diagonale dans ce cas) """
    
    def __init__(self,entree, sortie, position=None):
        self.depart =entree # entree est une porte
        self.arrivee=sortie # sortie est une porte
        self.position=position
        # soit le voyageur est deja sur la carte, soit il est a la porte d'entree
        
    def autourVoyageur(self):
        pass
    
    def deplacer(self):
        pass
        

