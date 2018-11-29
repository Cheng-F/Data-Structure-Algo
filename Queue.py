class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return (str(self.items))
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def isEmpty(self):
        return self.items == []
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


def potato(num,names):
    q = Queue()
    for name in names:
        q.enqueue(name)
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

print(potato(1,["Bill","David","Susan","Jane","Kent","Brad"]))
    
    
        
