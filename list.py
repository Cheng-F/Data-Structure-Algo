class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,new):
        temp = Node(new)
        temp.setNext(self.head)
        self.head = temp
        print (self.head)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and found == False:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current  = self.head
        previous = None
        found = False

        while not found:
            if current == None:
                return print('Not found the value to be deleted')
            elif current.getData() == item:
                 
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    
ul = UnorderList()
ul.add(1)
ul.add(10)
ul.add(2)

