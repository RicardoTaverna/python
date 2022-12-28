class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def add(self, data):
        """Use list append method to add elements."""
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    
    def remove(self):
        """Use list pop method to remove elements."""
        if len(self.stack) <= 0:
            return('No elements in the stack')
        else:
            return self.stack.pop()

    def peek(self):
        """Use peek to look at the top the stack."""
        return self.stack[-1]


aStack = Stack()
aStack.add('Mon')
aStack.add('Tue')
print(aStack.peek())
aStack.add('Wed')
aStack.add('Thu')
print(aStack.peek())
print(aStack.remove())
print(aStack.remove())
