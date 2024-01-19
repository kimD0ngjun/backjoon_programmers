import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack<Character> stack = new Stack<>();
        StringBuilder answer = new StringBuilder();

        int index = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < index; i++) {
            String ps = scanner.nextLine();

            for (char p : ps.toCharArray()) {
                if (p == '(') {
                    stack.push(p);
                } else {
                    if (!stack.isEmpty()) {
                        stack.pop();
                    } else {
                        stack.push(p); // 오답 체킹용 임의 푸시
                        break;
                    }
                }
            }

            if (!stack.isEmpty()) {
                answer.append("NO\n");
            } else {
                answer.append("YES\n");
            }

            // 스택 초기화를 잊지 말자....
            stack.clear();
        }

        System.out.println(answer);
    }
}
