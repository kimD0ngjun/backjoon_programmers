import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder stringBuilder = new StringBuilder();

        Stack<Integer> stack = new Stack<>();

        int index = scanner.nextInt();

        int top = 0;

        // index번 반복
        while(index != 0) {
            int value = scanner.nextInt();

            if (value > top) {
                for(int i = top; i < value; i++) {
                    stack.push(i + 1); // 기준 top 값 위의 값만큼 채워넣기
                    stringBuilder.append('+').append('\n');
                }
                top = value; // 쌓을 것인지, 뺄 것인지를 잇기 위한 기준 top 값 제시
            } else if (stack.peek() != value) {
                System.out.println("NO");
                System.exit(0);
            }

            stack.pop();
            stringBuilder.append('-').append('\n'); 
            // 다시 쌓든, 안 그렇든 일단 마지막은 pop은 한 번씩 이뤄져야 하므로.
            index--;
        }

        System.out.println(stringBuilder);
    }
}
