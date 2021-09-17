from node import Node
class CList:   
    def __init__(self): 
        self.head = None # CList의 마지막 노드
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)  
        if self.is_empty(): 
            temp.set_next(temp)
            self.head = temp
        else: 
            temp.set_next(self.head.get_next())  
            self.head.set_next(temp) 
            
    def append(self, item):
        temp = Node(item)  
        if self.is_empty(): 
            temp.set_next(temp)
            self.head = temp
        else: 
            temp.set_next(self.head.get_next())  
            self.head.set_next(temp)
            self.head = temp   
            
    def pop_first(self): 
        if self.head == None:
            print("List is empty.")
        else:
            temp = self.head.get_next()
            if temp == temp.get_next():   
                self.head = None
            else:
                self.head.set_next(temp.get_next())
            
    def search(self,item):
        if self.head == None:
            print("List is empty.")
        else:
            temp = self.head.get_next()
            if temp == temp.get_next():
                if temp.get_item() == item:
                    return True
                else:
                    return False
            found = False
            current = temp
            while True:
                if current.get_item() == item:
                    found = True
                else:
                    current = current.get_next()
                if current != temp and not found:
                    continue
                else:
                    break
            return found

if __name__ == "__main__":
    c = CList()
    c.is_empty()
    c.append(10)
    c.append(20)
    c.append(30)
    c.append(40)
    c.add(5)
    temp = c.head.get_next()
    current = temp 
    print(c.search(5), c.search(10), c.search(40), c.search(45))
    while True: 
        if current == c.head:
            print(current.get_item())
        else:
            print(current.get_item(),' -> ', end='')
        current = current.get_next()
        if current != temp:
            continue
        else:
            break