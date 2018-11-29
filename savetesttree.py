class BinaryTree:
    def __init__(self,node):
        self.node = node
        self.left_tree = None
        self.right_tree = None
    def __str__(self):
        return str([(self.node),['left tree: '+str(self.left_tree)],['right tree: '+str(self.right_tree)]])

    def leftInsert(self,left):
        if self.left_tree == None:
            self.left_tree = left
        else:
            t = BinaryTree(left)
            t.left_tree= self.left_tree
            self.left_tree = t

    def rightInsert(self,right):
        if self.right_tree == None:
            self.right_tree = right
        else:
            t = BinaryTree(right)
            t.right_tree = self.right_tree
            self.right_tree = t

    def getLeft(self):
        return self.left_tree
    def getRight(self):
        return self.right_tree
    def setRoot(self,root):
        self.node = root
    def getRoot(self):
        return self.node

 
pStack = []
pTree = BinaryTree("")

currentTree = pTree
 
 
pStack.append(currentTree)
#currentTree.leftInsert('')
pTree = BinaryTree(currentTree.getLeft())
        
pTree.setRoot('4')
currentTree = pStack.pop()
if currentTree.getLeft() == None:
    currentTree.leftInsert(pTree)
else:
    currentTree.rightInsert(pTree)
pStack.append(currentTree)


        
currentTree = pStack.pop() 
currentTree.setRoot('+')
pStack.append(currentTree)
pTree = BinaryTree(currentTree.getRight())


pTree.setRoot('6')
currentTree = pStack.pop()
if currentTree.getLeft() == None:
    currentTree.leftInsert(pTree)
else:
    currentTree.rightInsert(pTree)
pStack.append(currentTree)
##currentTree = pStack.pop()



