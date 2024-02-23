class Stack:
    def __init__(self):
        self.stack = []

    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False   
        
    def afficher(self):
        for i in self.stack:
            print(i)

    def peek(self): 
         return self.stack[-1]  
    def supprimer(self):
        if len(self.stack) <= 0:
            return ("pas d'element")
        else:
            return self.stack.remove()     

moi = Stack()
print(moi.add("tony"))
print(moi.add("yoni"))
print(moi.add("yni"))
print(moi.add(23))
print(moi.supprimer())
#print(moi.afficher())
print(moi.peek())