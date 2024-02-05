import java.util.*;

class MyStack {
    private ArrayDeque<Integer> queue;

    public MyStack() {
        this.queue = new ArrayDeque<>();
    }
    
    public void push(int x) {
        queue.add(x);
    }
    
    public int pop() {
        return queue.pollLast();
    }
    
    public int top() {
        return queue.peekLast();
    }
    
    public boolean empty() {
        return queue.isEmpty();
    }
}