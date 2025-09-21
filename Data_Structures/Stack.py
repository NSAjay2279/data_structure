class Stack:
  def __init__(self):
    self.storage = []
    self.count = 0

  def push(self, value):
    self.storage += [value]
    self.count += 1

  def pop(self):
    if self.count == 0:
      return None
    self.count -= 1
    result = self.storage[self.count]
    del self.storage[self.count]
    return result

  def size(self):
    return self.count

  def peek(self):
    return self.storage[self.count-1]

myStack = Stack()
myStack.push(1)
myStack.push(2)
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
