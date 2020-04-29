#-------------------------------------------------------------------------------
# Name:        module Python
# Purpose:     TP AB 
#
# Author: Lisa OULMI, 3A IBC
#
# Created:     29/04/2020
# Copyright:   (c) Loulmi2020
 
#-------------------------------------------------------------------------------

## nd = noeud droite
## ng = noeud gauche

class ArbreBinaire:
 ###################################################
    def __init__(self):
        self.noeud = None
        self.nd = None
        self.ng = None
 ###################################################
    def getNoeud(self):
        return self.noeud
    
    def setNoeud(self, noeud):
        self.noeud = noeud
 ###################################################
    def getNd(self):
        return self.nd

    def setNd(self, nd):
        self.nd = nd
 ###################################################
    def getNg(self):
        return self.ng

    def setNg(self, ng):
        self.ng = ng
 ###################################################
    def __str__(self):
        print (self.noeud)
        print (self.nd)
        print (self.ng)

###################################################
##Algorithme prefixe(Noeud)
##    1. La racine.
##    2. Parcours prefixe sous-arbre gauche.
##    3. Parcours prefixe sous-arbre droit.
        
    def prefixe(self, Arbre):
        if(Arbre == None):
            print("return")
            return
        print("racine",Arbre)
        if Arbre.ng!=None:
            self.prefixe(Arbre.ng)
        if self.nd!=None:
            self.prefixe(Arbre.nd)
    
 ######################affichage#############################
arbre = ArbreBinaire()
arbre.setNoeud(21)
arbre.setNd(14)
arbre.setNg(7)
##print(arbre.getNoeud())
print(arbre.__str__())
arbre.prefixe(arbre)


