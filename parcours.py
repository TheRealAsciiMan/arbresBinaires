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
        return self
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

def prefixe(arb: Noeud) -> str:
    ret = arb.etiquette
    if arb.gauche is not None:
        ret += " - " + prefixe(arb.gauche)
    if arb.droite is not None:
        ret += " - " + prefixe(arb.droite)
    return ret

def infixe(arb: Noeud) -> str:
    ret = ""
    if arb.gauche is not None:
        ret += infixe(arb.gauche) + " - "
    ret += arb.etiquette
    if arb.droite is not None:
        ret += " - " + infixe(arb.droite)
    return ret

def postfixe(arb: Noeud) -> str:
    ret = ""
    if arb.gauche is not None:
        ret += postfixe(arb.gauche) + " - "
    if arb.droite is not None:
        ret += postfixe(arb.droite) + " - "
    ret += arb.etiquette
    return ret

jaaj = Noeud("GP").ajoute_un_fils(Noeud("F1"), "g")
jaaj.gauche.ajoute_un_fils(Noeud("PF1"), "g")
jaaj.gauche.ajoute_un_fils(Noeud("PF2"), "d")
jaaj.ajoute_un_fils(Noeud("F2"), "d")
print(jaaj)
print(prefixe(jaaj))
print(infixe(jaaj))
print(postfixe(jaaj))