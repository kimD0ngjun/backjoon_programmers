import java.util.ArrayList;
import java.util.List;

class Solution {
    public String longestPalindrome(String s) {
        List<String> group = new ArrayList<>();

        if (s.length() <= 1) {
            return s;
        }

        // 홀수 펠린드롬
        for (int i = 0; i < s.length(); i++) {
            int left = i;
            int right = i;

            while(left >= 0 && right <= s.length() -1) {
                if (s.charAt(left) == s.charAt(right)) {
                    group.add(s.substring(left, right + 1));
                    left--;
                    right++;
                } else {
                    break;
                }
            }
        }

        // 짝수 펠린드롬
        for (int i = 0; i < s.length(); i++) {
            int left = i;
            int right = i + 1;

            while(left >= 0 && right <= s.length() -1) {
                if (s.charAt(left) == s.charAt(right)) {
                    group.add(s.substring(left, right + 1));
                    left--;
                    right++;
                } else {
                    break;
                }
            }
        }

        return group.stream()
                .max(Comparator.comparing(String::length)).orElse("");
    }
}
