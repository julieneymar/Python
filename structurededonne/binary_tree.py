class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def inserer(self , valeur):
        if self.data:
            if valeur < self.data:
                if self.left is None:
                    self.left = Node(valeur)
                else:
                    self.left.inserer(valeur)
            elif valeur > self.data:
                if self.right is None:
                    self.right = Node(valeur)
                else:
                    self.right.inserer(valeur)
        else:
            self.data = valeur                 
                
    def afficher(self):
        if self.left :
            self.left.afficher()
        print(self.data)
        if self.right:
            self.right.afficher()
       

    def trverse_in_order(self,racine):
        liste = []
        if racine:
            liste = self.trverse_in_order(racine.left)
            liste.append(racine.data)
            liste = liste + self.trverse_in_order(racine.right)
        return liste


    def traverser_pre_order(self, root):
        listes = []
        if root :
            listes.append (root.data)
            listes = listes + self.traverser_pre_order(root.left) 
            listes = listes + self.traverser_pre_order(root.right) 
        return listes
    
    def traverse_post_order(self,roots):
        lite = []
        if roots :
            lite = self.traverse_post_order(roots.left)
            lite = lite + self.traverse_post_order(roots.right)
            lite.append(roots.data)
        return lite    


    
dod = Node(12)
dod.inserer(13)
dod.inserer(14)
dod.inserer(11)
dod.inserer(10)
dod.inserer(15)
dod.afficher()
print(dod.trverse_in_order(dod))
print(dod.traverser_pre_order(dod))
print(dod.traverse_post_order(dod))
