#환형 연결 리스트로 구현한 큐 
from node import Node
class Queue:
    def __init__(self): 
        self.head = None 
        
    def is_empty(self):
        return self.head == None
    
    def enqueue(self, item):
        temp = Node(item)  
        if self.is_empty(): 
            temp.set_next(temp)
            self.head = temp
        else: 
            temp.set_next(self.head.get_next())  
            self.head.set_next(temp)
            self.head = temp   
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.head.get_next()
            dequeued_item = temp.get_item()
            if temp == temp.get_next():   
                self.head = None
            else:
                self.head.set_next(temp.get_next())
            return dequeued_item
    
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
 
    def size(self):
        count = 0
        if self.is_empty():
            return count
        temp = self.head.get_next()
        current = temp
        while True:
            count = count + 1
            current = current.get_next()
            if current != temp:
                continue
            else:
                break
        return count 
      
if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.is_empty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    