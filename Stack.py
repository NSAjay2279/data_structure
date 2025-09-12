class Stack:
  def __init__(self):
    self.num = []
    self.counter = 0
  
  def push(self, num):
    self.num += [num]
    self.counter += 1
    return

  def pop(self):
    n = len(self.num) - 1
    new = [None] * n
    for i in range(n):
      new[i] = self.num[i]
    self.num = new
    self.counter -= 1
    return self.num

  def peek(self):
    if len(self.num) == 0:
       return self.num
    return self.num[self.counter-1]

  def __str__(self):
    return str(self.num)


p = Stack()
p.push(1)
p.push(123)
p.push(23)
p.push("hi")
p.push("1")
print(p.pop())
print(p.peek())
print(p)
