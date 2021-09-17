from dnode import Node
class DList:   

    def __init__(self): 
        self.head = None

    def is_empty(self): return self.head == None
    
    def add(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            temp = Node(item)
            temp.set_next(self.head)
            self.head.set_previous(temp)
            self.head = temp
            
    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            temp = Node(item)
            current.set_next(temp)
            temp.set_previous(current)
            
    def insert_after(self, item, x):
        if self.head == None:
            print("List is empty.")
        else:
            current = self.head
            found = False
            while current != None and not found:
                if current.get_item() == x:
                    found = True
                else:
                    current = current.get_next()
            if found == False:
                print("Item is not in the list.")
            else:
                temp = Node(item)
                temp.set_next(current.get_next())
                temp.set_previous(current)
                if current.get_next() != None:
                    current.get_next().set_previous(temp)
                current.set_next(temp)  
                
    def insert_before(self, item, x):
        if self.head == None:
            print("List is empty.")
        else:
            current = self.head
            found = False
            while current != None and not found:
                if current.get_item() == x:
                    found = True
                else:
                    current = current.get_next()
            if found == False:
                print("Item is not in the list.")
            else:
                temp = Node(item)
                temp.set_next(current)
                temp.set_previous(current.get_previous() )
                if current.get_previous() != None:
                    current.get_previous().set_next(temp)
                else:
                    self.head = temp
                current.set_previous(temp)
                
    def pop_first(self):
        if self.head == None:
            print("List is empty.")
        else:
            if self.head.get_next() == None:
                self.head = None
            else:
                self.head = self.head.get_next()
                self.head.set_previous(None)
        
    def pop_last(self):
        if self.head == None:
            print("List is empty.")
        else:
            if self.head.get_next() == None:
                self.head = None
            else:
                current = self.head
                while current.get_next() != None:
                    current = current.get_next()
                current.get_previous().set_next(None)
         
    def delete(self, item):
        if self.head.get_item() == item:
            self.head = self.head.get_next()
            if self.head != None:
                self.head.set_previous(None)
        else:
            current = self.head
            found = False
            while not found:
                if current.get_item() == item:
                    found = True
                else:
                    current = current.get_next() 
            if current.get_next() != None:
                current.get_previous().set_next(current.get_next())
                current.get_next().set_previous(current.get_previous())
            else:
                current.get_previous().set_next(None)
                
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_item() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count 

if __name__ == "__main__":
    d = DList()
    d.add(10)
    d.add(30)
    d.add(40)
    d.insert_before(5, 10)
    d.insert_after(15, 10)
    d.delete(40)
    d.delete(15)
    current = d.head
    while current:
        if current.get_next() != None:
            print(current.get_item(), '<=> ', end = '')
        else:
            print(current.get_item())
        current = current.get_next()
   
    
    
    