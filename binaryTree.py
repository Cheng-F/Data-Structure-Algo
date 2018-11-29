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



def buildParseTree(pString):
    pList = pString.split()
    pStack = []
    pLvl = []
    currentTree = BinaryTree("")
    pStack.append(currentTree)
    pTree = BinaryTree(currentTree.getLeft())
   
    for i in pList:
        if i == '(':
            currentTree = BinaryTree('') 
            pStack.append(currentTree)
            pTree = BinaryTree(currentTree.getLeft())
            
        elif i in ['+','-','*','/']:
             
                
            currentTree = pStack.pop()
            if currentTree.getRoot() == '':
                currentTree.setRoot(i)
            else:
                pTree = BinaryTree(i)
                pTree.leftInsert(currentTree)
                currentTree = pTree
            pLvl.append(i) 
            pStack.append(currentTree)
            pTree = BinaryTree(currentTree.getRight())
        elif i not in ['+','-','*','/',')']:
            pTree.setRoot(i)
            currentTree = pStack.pop()
             
            if currentTree.getLeft() == None:
                currentTree.leftInsert(pTree)
            else:
                currentTree.rightInsert(pTree)
            pStack.append(currentTree)
        elif i == ')':
            currentTree = pStack.pop()
        else:
            currentTree = 'ERROR'
    return pStack


            


myTest = "(  5 + 6 )"    
myString = "4 + (  5 + 6 ) * ( 7 + 8 )"
alist = myTest.split()





