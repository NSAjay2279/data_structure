class Node {
  int data;
  Node next;

  Node(int data) {
    this.data = data;
    this.next = null;
  }
}

class Stack {
  private Node top;

  Stack() {
    top = null;
  }


  // Push oepration (O(1))
  public void push(int value) {
    Node newNode = new Node(value);
    newNode.next = top;
    top = newNode;
  }

  // Pop operation (O(1))
  public int pop() {
    if (top == null) {
      System.out.println("Stack Underflow");
      return -1;  // Error value
    }
    int popped = top.data;
    top = top.next;
    return popped;
  }

  // Peek operation (O(1))
  public int peek() {
    if (top == null) {
      System.out.println("Stack is empty");
      return -1;  // Error value
    }
    return top.data;
  }

  // Check if stack is empty
  public boolean isEmpty() {
    return top == null;
  }

}

public class StackDemo {
  public static void main(String[] args) {
    Stack stack = new Stack();

    stack.push(10);
    stack.push(20);
    stack.push(30);

    System.out.println("Top element: " + stack.peek()); // 30
    System.out.println("Popped: " + stack.pop());       // 30
    System.out.println("Top element: " + stack.peek()); // 20

    System.out.println(stack);
  }
}
