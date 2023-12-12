class Noeud:
    def __init__(self, etiquette:str):
        self.etiquette = etiquette
        self.gauche = None
        self.droite = None
    def ajoute_un_fils(self, noeud, pos:str):
        if pos == "g":
            self.gauche = noeud
        elif pos == "d":
            self.droite = noeud
    def __str__(self) -> str:
        if self.gauche == None and self.droite == None:
            return self.etiquette
        else :
            ma_liste = self.etiquette + '('
            ma_liste += ' '
            ma_liste += self.gauche.__str__()
            ma_liste += ' '
            ma_liste += self.droite.__str__()
            ma_liste += " )"
            return ma_liste

    def hauteur(self) -> int:
        if self.gauche is None and self.droite is None:
            return 0
        if self.gauche:
            hauteur_gauche = self.gauche.hauteur()
        else:
            hauteur_gauche = 0

        if self.droite:
            hauteur_droite = self.droite.hauteur()
        else:
            hauteur_droite = 0
        return max(hauteur_gauche, hauteur_droite) + 1
    def feuilles(self) -> int:
        if self.gauche is None and self.droite is None:
            return 1
        if self.gauche:
            nombre_feuilles_gauche = self.gauche.feuilles()
        else:
            nombre_feuilles_gauche = 0

        if self.droite:
            nombre_feuilles_droite = self.droite.feuilles()
        else:
            nombre_feuilles_droite = 0
        return nombre_feuilles_gauche + nombre_feuilles_droite


    def noeuds_internes(self) -> int:
        if self.gauche is None and self.droite is None:
            return 0
        if self.gauche:
            nombre_noeuds_internes_gauche = self.gauche.noeuds_internes()
        else:
            nombre_noeuds_internes_gauche = 0

        if self.droite:
            nombre_noeuds_internes_droite = self.droite.noeuds_internes()
        else:
            nombre_noeuds_internes_droite = 0
        return nombre_noeuds_internes_gauche + nombre_noeuds_internes_droite + 1
def taille(arbre) -> int:
    if arbre is None:
        return 0
    return 1 + taille(arbre.gauche) + taille(arbre.droite)


A = Noeud("A")
B = Noeud("B")
C = Noeud("C")
D = Noeud("D")
E = Noeud("E")
F = Noeud("F")
G = Noeud("G")
H = Noeud("H")
I = Noeud("I")
J = Noeud("J")
K = Noeud("K")
L = Noeud("L")
M = Noeud("M")
N = Noeud("N")
O = Noeud("O")
P = Noeud("P")
Q = Noeud("Q")


A.ajoute_un_fils(B, "g")
A.ajoute_un_fils(C, "d")
B.ajoute_un_fils(D, "g")
B.ajoute_un_fils(E, "d")
E.ajoute_un_fils(H, "g")
E.ajoute_un_fils(I, "d")
I.ajoute_un_fils(N, "g")
I.ajoute_un_fils(O, "d")
C.ajoute_un_fils(F, "g")
C.ajoute_un_fils(G, "d")
F.ajoute_un_fils(J, "g")
F.ajoute_un_fils(K, "d")
G.ajoute_un_fils(L, "g")
G.ajoute_un_fils(M, "d")
M.ajoute_un_fils(P, "g")
M.ajoute_un_fils(Q, "d")
print(A)
print(taille(A))
