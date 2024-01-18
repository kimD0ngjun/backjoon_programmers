import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StringBuilder stringBuilder = new StringBuilder();

        Stack<Integer> stack = new Stack<>();

        int index = scanner.nextInt();
        int top = 0;

        while (index-- > 0) {
            int value = scanner.nextInt();
            top = processValues(value, top, stack, stringBuilder);
        }

        System.out.println(stringBuilder);
    }

    private static int processValues(int value, int top, Stack<Integer> stack, StringBuilder stringBuilder) {
        if (value > top) {
            for (int i = top; i < value; i++) {
                stack.push(i + 1);
                stringBuilder.append('+').append('\n');
            }
            top = value;
        } else if (stack.peek() != value) {
            System.out.println("NO");
            System.exit(0);
        }

        stack.pop();
        stringBuilder.append('-').append('\n');
        return top;
    }
}
