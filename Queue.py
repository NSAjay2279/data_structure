class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if not self.front:
            return None
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return data
    
    def peek(self):
        return self.front.data if self.front else None
    
    def is_empty(self):
        return self.front is None
    
    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    print("Peek:", queue.peek())
    print("Dequeue:", queue.dequeue())
    queue.display()