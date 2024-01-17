import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        stack.add(arr[0]);

        int index = 1;

        while (index != arr.length) {
            int lastNumber = stack.peek();
            stack.add(arr[index]);

            if (lastNumber == stack.peek()) {
                stack.pop();
            }

            index++;
        }

        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }

        return result;
    }
}