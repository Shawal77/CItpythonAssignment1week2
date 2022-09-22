class Stack:
    def __init__(self):
        self.stack = list()
    def push(self, data):
        # push element on the stack
        self.stack.append(data)
    def pop(self):
        # pop element from the stack
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()
    def size(self):
        return len(self.stack)