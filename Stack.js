class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
  }

  // Push operation (O(1))
  push(value) {
    const newNode = new Node(value);
    newNode.next = this.top;
    this.top = newNode;
  }

  pop() {
    if (this.top === null) {
      console.log("Stack Underflow");
      return -1;  // Error value
    }
    const popped = this.top.data;
    this.top = this.top.next;
    return popped;
  }

  // Peek operation (O(1))
  peek() {
    if (this.top === null) {
      console.log("Stack is empty");
      return -1;  // Error value
    }
    return this.top.data;
  }

  // Check if stack is empty
  isEmpty() {
    return this.top === null;
  }


}

const stack = new Stack();

stack.push(10);
stack.push(20);
stack.push(30);

console.log("Top element:", stack.peek());  // 30
console.log("Popped:", stack.pop());        // 30
console.log("Top element:", stack.peek());       // 20
