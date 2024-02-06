import java.util.*;

class MyQueue {
    private ArrayDeque<Integer> stack;
    
    public MyQueue() {
        this.stack = new ArrayDeque<>();
    }
    
    public void push(int x) {
        stack.add(x);
    }
    
    public int pop() {
        return stack.poll();
    }
    
    public int peek() {
        return stack.peek();
    }
    
    public boolean empty() {
        return stack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */