import functools as ft
import random
import environnement
from astropy.table import row

class Grille:
    """
    Représente le 'terrain' où évoluent les éléments de la simulation.
    Une grille est créée vierge puis ont lui ajoute différents éléments qui 
    occupent sur une ou plusieurs coordonnées.
    Les liens entre objets et coordonnées est maintenu par des dictionnaires 
    Une coordonnée non occupée est juste asbente des clefs.
    Les objets mobiles (voyageurs) dialoguent avec la grille au travers de 
    différentes méthodes
    """
    def  __init__(self):
        """ 
        voyageurs, obstacles et portent sont conservés dans trois attributs 
        différents, de type dictionnaire avec des coordonnées (couple de int)
        comme clefs
        """
        self.voyageurs = dict()
        self.obstacles = dict()
        self.portes = dict()
        
    def addVoyageur(self, coord, v):
        """
        Ajoute un voyageur,sur UNE certaine coordonnée, dans le dictionnaire
        des voyageurs.
        """
        assert(coord not in self.voyageurs.keys())
        self.voyageurs[coord] = v
    
    def addObstacle(self, coords, m):
        """
        Ajoute un obstacle,sur certaineS coordonnéeS, dans le dictionnaire
        des obstacles.
        """
        for coord in coords:
            assert coord not in self.obstacles.keys(), str(coord) + " occupée"
            self.obstacles[coord] = m
    
    def addPorte(self, coords, p):
        """
        Ajoute une porte,sur certaineS coordonnéeS, dans le dictionnaire
        des portes.
        """
        for coord in coords:
            assert(coord not in self.portes.keys())
            self.portes[coord] = p
    
    def getVoyageurs(self):
        """
        Retourne le dictionnaire des voyageurs.
        Il sera aproprié, ultérieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.voyageurs
    
    def getObstacles(self):
        """
        Retourne le dictionnaire des obstacles.
        Il sera aproprié, ultérieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.obstacles
    
    def getPortes(self):
        """
        Retourne le dictionnaire des portes.
        Il sera aproprié, ultérieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.portes
    
    def getPosition(self, v):
        """
        Retourne la position d'un voyageur donné du dictionnaire
        des voyageurs
        """
        assert (v in self.voyageurs.values())
        for coord in self.voyageurs.keys():
            if self.voyageurs[coord] == v:
                return coord
    
    def setPosition(self, v, coord):
        """
        Assigne une nouvelle position à un voyageur donné du dictionnaire
        des voyageurs
        """
        positionActuelle = self.getPosition(v)
        assert(coord not in self.voyageurs.keys())
        assert(coord not in self.obstacles.keys())
        self.voyageurs[coord] = self.voyageurs.pop(positionActuelle)
    
    def getContenuCase(self, coord):
        """
        Retourne le (ou les) contenus d'une case donnée.
        A noter que sur une case donnée il peut y avoir un voyageur ET une porte
        """
        mbv = self.voyageurs.get(coord, None)
        mbo = self.obstacles.get(coord, None)
        mbp = self.portes.get(coord, None)
        return (mbv, mbo, mbp)
    
    def getDirection(self, v, p):
        """
        Retourne le vecteur d'origine un voyageur donné et d'extrémité
        le point moyen d'une porte donnée
        """
        coords = [coord for coord in self.portes if (self.portes[coord] == p)]
        size = len(coords)
        assert(size != 0)
        (sx, sy) = (0, 0)
        for (x, y) in coords:
            sx += x
            sy += y
        (vx, vy) = self.getPosition(v)
        return ((sx / size) - vx, (sy / size) - vy)
        
    def deleteVoyageur(self, v):
        """
        Commande à la grille "d'oublier" un voyageur donné
        """
        position = self.getPosition(v)
        self.voyageurs.pop(position)
        
    def deplacements(self):
        """
        Active un 'tour' de placement pour chaque voyageur présent dans
        la grille
        """
        # ne pas iterer sur un objet que l'on modifie !
        # A FAIRE : mélanger auparavent la liste des voyageurs
        voys = [self.voyageurs[coord] for coord in self.voyageurs.keys()]
        for v in voys:
            v.seDeplacer()
            
    def __str__(self) -> str:
        """
        Représentation textuelle sommaire de la grille
        """
#         coords = self.obstacles.keys()
        minx = min([coords[0] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
        maxx = max([coords[0] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
        miny = min([coords[1] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
        maxy = max([coords[1] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
        txt = ""
        for y in range(miny, maxy + 1):
            row = ""
            for x in range(minx, maxx + 1):
                v = self.voyageurs.get((x, y), None)
                m = self.obstacles.get((x, y), None)
                p = self.portes.get((x, y), None)
                if v != None:
                    row += 'v'
                elif m != None:
                    row += 'o'
                elif p != None:
                    row += 'p'  
                else:
                    row += "."  
            row += "\n"
            txt += row
        return txt