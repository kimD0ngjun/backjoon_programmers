import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        StringBuilder answer = new StringBuilder();

        for (char p : s.toCharArray()) {
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
            return false;
        } else {
            return true;
        }        
    }
}