class Queue:
    def __init__(self):
        self.queue = list()
    def enqueue(self, data):
        self.queue.insert(0, data)
        return True
    def dequeue(self):
        if self.isEmpty():
            return ("Queue is empty!")
        return self.queue.pop()
    def size(self):
        return len(self.queue)
'/'