class Stack:
     def __init__(self):
         self.items = []
     def __str__(self):
         return str(self.items)
     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
infixexpr = 'A + ( B - C ) * D * G + E * F'        
prec = {}
prec["*"] = 3
prec["/"] = 3
prec["+"] = 2
prec["-"] = 2
prec["("] = 1
opStack = Stack()
postfixList = []
tokenList = infixexpr.split()

for token in tokenList:
    if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
        postfixList.append(token)
        print ('postfixList append ' + token)
    elif token == '(':
        opStack.push(token)
        print ('opStack push '+ token)
    elif token == ')':
        topToken = opStack.pop()
        print ('opStack pop tp topToken' + topToken)
        while topToken != '(':
            postfixList.append(topToken)
            topToken = opStack.pop()
            print ('postfixList append and opStack pop '+ topToken)
    else:
        while (not opStack.isEmpty()) and \
           (prec[opStack.peek()] >= prec[token]):
              postfixList.append(opStack.pop())
              print ('postfixList append (opStack pop), opStack: '+ str(opStack))
        opStack.push(token)
        print ('opStack push' + token)

while not opStack.isEmpty():
    postfixList.append(opStack.pop())
    print ('postfixList append opStack pop,opStack:'+ str(opStack))
print('results '+ "".join(postfixList))
print('input: '+infixexpr)
