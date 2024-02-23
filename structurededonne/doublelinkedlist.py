class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_linked_list:
    def __init__(self):
        self.head = None

    def ajouter(self,newval):
        newNode = Node(newval)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def afficher(self):
        value = self.head
        while(value is not None):
            print(value.data)
            last = value
            value = value.next

    def ajoute_millieu(self,exist,entrer):
       current = self.head
       while current is not None:
           if current .data == exist:
               newvalue = Node(entrer)
               newvalue.next = current.next
               current.next = newvalue
               newvalue.prev = current
               if newvalue.next is not None:
                   newvalue.next.prev = newvalue
                   break
           current = current.next


           
    def alafin(self,valeur):
        newvaleur = Node(valeur)
        newvaleur.next = None
        if self.head is None:
            newvaleur.prev = None
            self.head = None
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = newvaleur
        newvaleur.prev = last
        return


notrelist = Doubly_linked_list()
notrelist.ajouter(10)
notrelist.ajouter(11)
notrelist.ajouter(12)
notrelist.ajouter(14)
notrelist.ajouter(15)
notrelist.afficher()
print("\n")
notrelist.ajoute_millieu(15,13)
notrelist.afficher()
notrelist.alafin(17)
notrelist.afficher()

