import java.util.*;

// 스택은 요소를 빼든, 넣든, 넣는 과정은 무조건 오름차순으로 이뤄진다.
// 그러므로 넣지 않고 연이어서 빼는 과정은 당연히 내림차순으로 이뤄져야 한다.

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
            }
                // 기준 top값이 입력 value값보다 크다는 것은(즉, if문 조건을 충족하지 못한 경우는)
                // (같다는 조건은 나올 수 없다. 정수는 중복되지 않으므로)
                // 내림차순으로 위에서부터 쌓여있는 것들을 하나하나씩 빼야 된다는 뜻이다
                // 그래서 마지막에 stack.pop()이 존재한다
            else if (stack.peek() != value) {
                // 가장 큰 수 이후로 내림차순으로 입력이 이뤄지지 않으면 NO!
                System.out.println("NO");
                System.exit(0);
            }

            stack.pop();
            stringBuilder.append('-').append('\n'); 
            // 다시 쌓든, 안 그렇든 일단 마지막은 pop은 한 번씩 이뤄져야 하므로
            // 이미 입력(value)으로 소진된 값은 빠지고 더 이상 스택에 관여하지 않는다
            index--;
        }

        System.out.println(stringBuilder);
    }
}
