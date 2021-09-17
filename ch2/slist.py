from node import Node
class SList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            self.head = temp
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(temp)
                
    def pop_first(self):
        self.head = self.head.get_next()
    
    def pop_last(self):
        current = self.head
        previous = None
        while current.get_next() != None:
            previous = current
            current = current.get_next()
        previous.set_next(None)
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count 
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_item() == item:
                found = True
            else:
                current = current.get_next()
        return found


    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_item() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
if __name__ == "__main__":
    s = SList()
    s.append(95)
    s.append(30)
    s.append(45)
    s.append(15)
    s.add(20)
    s.delete(15)
    s.pop_first()
    s.pop_last()

    print(s.size())
    current = s.head
    while current:
        if current.get_next() != None:
            print(current.get_item(), '->', end = '')
        else:
            print(current.get_item())
        current = current.get_next()
 
    
    