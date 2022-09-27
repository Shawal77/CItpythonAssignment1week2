#push first check if full
#pop first check if empty
#is empty

class stack:
    def __init__(self):
        self.stack = list()
    def isEmpty(self):
        # check if the stack is empty
        return len(self.stack) == 0

    def push(self, data):
        # push element on the stack
        self.stack.append(data)
        
    def peek(self):
        # Use peek to look at the top of the stack
        return self.stack[-1]

    def pop(self):
        # pop element from the stack
        if self.isEmpty():
            return ("Stack is empty. Stack Underflow :(")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

