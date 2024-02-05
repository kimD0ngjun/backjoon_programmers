from collections import deque

class MyStack:

    def __init__(self): # 생성자
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# import java.util.*;

# class MyStack {
#     private ArrayDeque<Integer> queue;

#     public MyStack() {
#         this.queue = new ArrayDeque<>();
#     }
    
#     public void push(int x) {
#         queue.add(x);
#     }
    
#     public int pop() {
#         return queue.pollLast();
#     }
    
#     public int top() {
#         return queue.peekLast();
#     }
    
#     public boolean empty() {
#         return queue.isEmpty();
#     }
# }