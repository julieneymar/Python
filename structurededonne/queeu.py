class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            return False
        
    def affiche(self):
        for a in self.queue:
            print(a)   

    def taille(self):
        return len(self.queue) 
    def suprim(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return ("no element")


poi = Queue()
poi.addtoq("papa")
poi.addtoq("maman")
poi.addtoq("ptit")
poi.addtoq("tta")
poi.addtoq(14)
print(poi.affiche())
print(poi.taille())
print(poi.suprim())
print(poi.taille())
print(poi.affiche())

