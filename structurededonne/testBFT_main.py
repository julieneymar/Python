#Breadth-First Traversal of a Binary Tree - www.101computing.net/breadth-first-traversal-of-a-binary-tree
# 
# from Tree import drawTree #This library will only be used to draw the binary tree on the screen

#A class to implement a Node / Tree
class Node:
    def __init__(self, aValue, aLeft=None, aRight=None):
        self.value = aValue
        self.left = aLeft
        self.right = aRight
    
# Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print( self.value)
        if self.right:
            self.right.printTree()

# Inorder traversal
# Left -> Root -> Right
    def inOrder(self):
        res = []
        if self.left:
            res = res + self.left.inOrder()
        res.append(self.value)
        if self.right:
             res = res + self.right.inOrder()
        return res

    def inOrderV2(self):
        res = []
        if self:
            res.append(self.value)
            res = res + self.left.preOrder()
            res = res + self.right.preOrder()
        return res


# PreOrder traversal
#  Root -> Left -> Right
    def preOrder(self):
        res = []
        res.append(self.value)
        if self.left:
            res = res + self.left.preOrder()
        if self.right:
             res = res + self.right.preOrder()
        return res
    
    def preOrderV2(self):
        res = []
        if self:
            res.append(self.value)
            res = res + self.left.preOrder()
            res = res + self.right.preOrder()
        return res
    
# PostOrder traversal
#  Left -> Right -> Root  
    def postOrder(self):
        res = []
        if self.left:
            res = res + self.left.postOrder()
        if self.right:
             res = res + self.right.postOrder()
        res.append(self.value)
        return res
    
    def breadthFirst(self):
        if self is None:  return
        file = []
        file.append(self)
        while(len(file) > 0):
            # afficher et retirer le premier élément
            print(file[0].value)
            node = file.pop(0)
            # ajouter l'enfant gauche de l'élément retiré
            if node.left is not None:
                file.append(node.left)
            # ajouter l'enfant droit de l'élément retiré
            if node.right is not None:
                file.append(node.right)


        def bfrfromLevel (self, Noode):
            h = self.height(node)
            res = []
            for i in range ( 1 , h+1):
                res = res + self.printLevel(node, i)
            return res
        
        def printlLevel (self, node, level):
            res = []
            if (node is None):
                return res 
            if (level == 1 ):
                #print(node.value)
                res.append(node.value)



    def sizeTree(self,root):
        #cas de base
        if root is None:
            return 0
        else:
            return 1 + self.sizeTree(root.left) + self.sizeTree(root.right)
        

    def height ( self, root):
        if root is None :
            return 0
        else :
            return 1 + max (self.height(root.left), self.height(root.right))

#Let's initialise our binary tree:
tree = Node(47) #The root node of our binary tree
tree.left = Node(36)
tree.right = Node(66)

tree.left.left = Node(25)
tree.left.right = Node(39)
tree.left.right.left = Node(38)
tree.left.right.right = Node(42)

tree.right.left = Node(63)
tree.right.left.right = Node(64)
tree.right.right = Node(68)

tree.printTree()
print (tree.inOrder())
print (tree.preOrder())
print (tree.postOrder())

print(tree.breadthFirst())
# drawTree(tree)

# #---> Implementation of the Breadth-First Traversal:
# 
# #We first initialise a queue with a single node: the root of the tree
# print("\n---> Breath First Traversal:")
# queue = [tree]
# values = []
# while len(queue)!=0:
#   #Dequeue the first node
#   currentNode = queue.pop(0)
#   #Read the node value:
#   values.append(currentNode.value)
#   
#   #Enqueue child nodes (if any)
#   if currentNode.left!=None:
#     #Enqueue the left node at the end of the queue:
#     queue.append(currentNode.left)
#   if currentNode.right!=None:
#     #Enqueue the right node at the end of the queue:
#     queue.append(currentNode.right)
#     
# #The end, let's print the list of values resulting from the breadth first traversal of our tree:
# print(values)
# 
# value = int(input("Type a value to search for..."))
# 
# #Binary Search...
# node = tree
# found=False
# while node!=None:
#   if value==node.value:
#     found=True
#     print("Yeah value found!")
#     break
#   elif value<node.value:
#     node = node.left
#   elif value>node.value:
#     node = node.right
#   
# if found==False:
#   print("Not found")

  
  
  
  