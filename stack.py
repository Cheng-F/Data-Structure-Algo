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



def parCheck(pstring):
    s = Stack()
    balanced = True
    index = 0
    while index < len(pstring) and balanced:
        if pstring[index] == '(':
            s.push('(')
            #print (s,balanced)
        else:
            if pstring[index] == ')' and s.isEmpty():
                balanced = False
            else:
                if pstring[index] == ')':
                    s.pop()
                    #print (s)
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
         
        return False
    
