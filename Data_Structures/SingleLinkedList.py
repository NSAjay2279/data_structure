class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class SingleLinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0
   
   def append(self, data):
      node = Node(data)
      if self.tail != None:
         self.tail.next = node
         self.tail = node
         return  
      self.head = node
      self.tail = node
      self.tail.next = None
      
   def length(self):
        current = self.head
        if current != None:
            self.size += 1
            while current.next:
               self.size += 1
               current = current.next
        else:
            return 0
        return self.size
      
   def __str__(self):
        list = []
        current = self.head
        if current != None:
            list.append(current.data)
            while current.next:
                current = current.next
                list.append(current.data)
            return str(list)
        else:
            return str(list)

      
words = SingleLinkedList()
words.append(1)
words.append(2)
words.append(3)
words.append(3)
print(words)
print(words.length())
