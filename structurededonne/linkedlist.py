class Node:
    def __init__(self, aData = None):
        self.data = aData
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listPrint(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next

    def sommet(self,date):
        newdata = Node(date)
        newdata.next = self.head
        self.head = newdata     

    def alafin (self,datefin):
        newdat = Node(datefin)
        if self.head is None :
            self.head = newdat
            return 
        laste = self.head
        while laste.next  :
            laste = laste.next
        laste.next = newdat

    def milieu(self, entrer, nouvelleentrer):
        if entrer is None :
            print (" absent")
            return
        mille = Node(nouvelleentrer)
        mille.next = entrer.next 
        entrer.next = mille

    def supprimer(self,suprimecle):
        valeursup = self.head
        if valeursup is not None :
            if valeursup.data == suprimecle :
                self.head = valeursup.next
                valeursup = None
                return
        while valeursup is not None :
            if valeursup.data == suprimecle :
                break
            prev = valeursup
            valeursup = valeursup.next
            if valeursup == None :
                return
            prev.next = valeursup.next 
            valeursup = None



alist = LinkedList()

alist.head = Node("Lundi")
e2 = Node("Mardi")
e3 = Node("Mercredi")
e4 = Node("Jeudi")
e5 = Node("Vendredi")
e6 = Node("Samedi")
e7 = Node("Dimanche")

alist.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
alist.listPrint()
alist.sommet("Monday")
alist.listPrint()
       


