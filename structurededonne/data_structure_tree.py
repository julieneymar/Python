class Node:
    def __init__(self,theName):
        self.name = theName
        self.children = []
        self.parent = None
    
    def addchild(self,node):
        node.parent = self
        self.children.append(node)

    def _listwithlevels(self,level,tress):
        tress.append("   " * level + str(self.name))
        for child in self.children:
            child._listwithlevels(level + 1, tress)

    def __str__(self):
        trees = []
        self._listwithlevels(0,trees)
        return "  \n".join(trees)
    

def printtree(node):
    print(node.name)
    for child in node.children:
        printtree(child)


root = Node("sara")
root.addchild(Node("jean"))
lucNode = Node("Luc")
root.addchild(lucNode)
root.addchild(Node("Marc"))
print(str(root))
#printtree(root)
# Luc children definition or creation

lucNode.addchild(Node("Loic"))
#lucNode.addchild(Node("Lola"))
lolaNode = Node("Lola")
lucNode.addchild(lolaNode)
lucNode.addchild(Node("Louis"))
#lucNode.addchild(Node("Lili"))
liliNode = Node("Lili")
lucNode.addchild(liliNode)
#lolachildren
lolaNode.addchild(Node("Nira"))
lolaNode.addchild(Node("Niro"))
#lilichildren
liliNode.addchild(Node("Mael"))
liliNode.addchild(Node("Joel"))





print(str(root))