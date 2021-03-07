class Node:
    def __init__(self, item):
        self.item = item  # data field
        self.next = None  # link field
        self.previous = None  # link field

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_item(self, new_item):
        self.item = new_item

    def set_next(self, new_next):
        self.next = new_next

    def set_previous(self, new_previous):
        self.previous = new_previous
