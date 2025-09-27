class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class QueueNode:
    def __init__(self, data=None):
        self.data = data  # 2
        self.next = None  # 

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root: # intitally root references to None object
            self.root = TreeNode(val) # now, root references to Tree object (with val ref. to 1<int type object>, left ref. to None, right ref. to None) 
            return
        queue = Queue() # queue object with front ref. to None, rear ref. to None
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            if not node.left:
                node.left = TreeNode(val)
                return
            elif not node.right:
                node.right = TreeNode(val)
                return
            queue.enqueue(node.left)
            queue.enqueue(node.right)

    def inorder(self, node, result=None):
      if result is None:
          result = []
      if node:
          self.inorder(node.left, result)
          result.append(node.val)
          self.inorder(node.right, result)
      return result


    def preorder(self, node, result=None):
      if result is None:
          result = []
      if node:
          result.append(node.val)
          self.preorder(node.left, result)
          self.preorder(node.right, result)
      return result

    def postorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)
        return result


    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node.val)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return result


    def search(self, val):
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.val == val:
                return True
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return False


    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1
    
    def delete(self, val):
        if not self.root:
            return
        if self.root.val == val and not self.root.left and not self.root.right:
            self.root = None
            return
        queue = Queue()
        queue.enqueue(self.root)
        target = None
        last = None
        while not queue.is_empty():
            node = queue.dequeue()
            if node.val == val:
                target = node
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            last = node
        if target:
            target.val = last.val
            self._delete_deepest(last)
    
    def _delete_deepest(self, node):
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            temp = queue.dequeue()
            if temp is node:
                temp = None
                return
            if temp.right:
                if temp.right is node:
                    temp.right = None
                    return
                else:
                    queue.enqueue(temp.right)
            if temp.left:
                if temp.left is node:
                    temp.left = None
                    return
                else:
                    queue.enqueue(temp.left)
    
    def insert_bst(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        current = self.root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    return
                current = current.right
    
    def search_bst(self, val):
        current = self.root
        while current:
            if current.val == val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False
    
    def size(self, node):
        if not node:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)
    
    def min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current.val if current else None
    
    def max_value(self, node):
        current = node
        while current.right:
            current = current.right
        return current.val if current else None


if __name__ == "__main__":
    tree = Tree() # tree references to Tree object
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    print("Inorder:", tree.inorder(tree.root))
    print("Level order:", tree.level_order())
    print("Search 2:", tree.search(2))
    print("Height:", tree.height(tree.root))