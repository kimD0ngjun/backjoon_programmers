import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int size = scanner.nextInt();
        
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 1; i <= size; i++) {
            queue.add(i);
        }
        
        while(queue.size() > 1) {
            int pollNumber = queue.poll();
            int backNumber = queue.poll();
            
            queue.add(backNumber);
        }
        
        System.out.println(queue.poll());
    }
}