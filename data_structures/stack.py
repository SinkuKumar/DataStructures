class Stack:
    __name__ = "Stack"

    def __init__(self):
        self.stack = []

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        self.stack.pop()

    def clear(self):
        self.stack.clear()

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return "Stack"

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.pop()
    my_stack.push(30)
    print(my_stack)
    print(type(my_stack))
    print(len(my_stack))
