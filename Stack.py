class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        return self.top.data if self.top else None
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    stack = Stack() # stack object
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    stack.display()