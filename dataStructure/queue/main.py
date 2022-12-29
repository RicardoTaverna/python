class Queue:
    def __init__(self) -> None:
        self.queue = list()

    def add(self, data):
        """Insert method to add elements."""
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False
    
    def remove(self):
        """Pop method to remove elements."""
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")
    
    def size(self):
        return len(self.queue)

    def printQueue(self):
        if len(self.queue) > 0:
            for element in self.queue:
                print(element)
        return ("No elements in Queue!")


new_queue = Queue()
new_queue.add('Mon')
new_queue.add('Tue')
new_queue.add('Wed')
new_queue.printQueue()
new_queue.remove()
print()
new_queue.printQueue()
