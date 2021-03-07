from node import Node


class CList:
    def __init__(self):
        self.head = None

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

    def delete(self, item):
        if self.head.get_item() == item:
            self.head = self.head.get_next()
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

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        if self.head == None:
            print("List is empty.")
        else:
            temp = self.head.get_next()
            if self.head == temp:
                if self.head.get_item() == item:
                    return True
                else:
                    False
        current = temp
        found = False
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
