class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data): # data = 1
        new_node = Node(data)   
        # Space complexity = O(1)
        # node object with data = 1, next = None
        # node object with data = 2, next = None
        # node object with data = 3, next = None
        if not self.head:   # intially True
            self.head = new_node    # head references 1st node object
            return
        current = self.head # current/head -> [1, None]
        # currrent/head -> [1, [2, None]]
        while current.next: # false
        # Time complexity = O(n)
            current = current.next  # current = [2, None]
        current.next = new_node # [1, [2, [3, None]]]
    
    def delete(self, data): # data = 2
        if not self.head:   # [1, [2, [3, None]]]
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head # [1, [2, [3, None]]]
        while current.next: # [2, [3, None]]
            if current.next.data == data:   # True
                current.next = current.next.next    # [3, None]
                # current = [1, [2, [3, None]]] 
                # self.head = [1, [2, [3, None]]]
                # current.next = [3, None]
                # current = [1, [3, None]]
                return
            current = current.next
    
    def search(self, data): # data = 2
        current = self.head # [1, [2, [3, None]]]
        while current:  # [2, [3, None]]
            if current.data == data:    # 1 = 1?
                return True
            current = current.next  
        return False
    
    def display(self):
        current = self.head # [1, [2, [3, None]]]
        while current:
            print(current.data, end=" -> ") # 1 -> 2 -> 3 -> None 
            current = current.next  # [2, [3, None]]
        print("None")

if __name__ == "__main__":
    ll = LinkedList()   # object with head = None
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.display()
    print("Search 2:", ll.search(2))
    ll.delete(2)
    ll.display()