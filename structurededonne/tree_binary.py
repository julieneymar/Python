class Node:
    def  __init__(self, aValue, aLeft = None, aRight = None):
        self.value = aValue
        self.left = aLeft
        self.right = aRight



    def print_Tree(self):
        if self.left :
            self.left.print_Tree()   
        print(self.value) 

        if self.right:
            self.right.print_Tree()
            


tree = Node(47)
tree.left = Node(36)
tree.right = Node(66)

tree.left.left = Node (25)
tree.left.right = Node(39)
tree.left.left = Node(38)
tree.left.right = Node (42)

tree.right.left = Node(63)
tree.right.right = Node(68)
tree.right.left = Node(64)

print(tree.print_Tree())

    