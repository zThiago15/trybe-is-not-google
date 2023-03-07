from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        return self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError('Index out of range in list')
            
        return self.items[index]
