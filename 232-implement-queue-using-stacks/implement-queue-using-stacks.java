import java.util.Stack;

class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    // Push element to the back of queue
    public void push(int x) {
        stack1.push(x);
    }

    // Removes element from front of queue
    public int pop() {
        shiftStacks();
        return stack2.pop();
    }

    // Get front element
    public int peek() {
        shiftStacks();
        return stack2.peek();
    }

    // Returns true if queue is empty
    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }

    // Helper method: Move elements from stack1 to stack2 if stack2 is empty
    private void shiftStacks() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
    }

    public static void main(String[] args) {
        MyQueue myQueue = new MyQueue();
        myQueue.push(1);
        myQueue.push(2);
        System.out.println(myQueue.peek());  
        System.out.println(myQueue.pop());    
        System.out.println(myQueue.empty());  
    }
}
