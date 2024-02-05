import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> check = new HashMap<>();
        int size = check.size();

        for(int i = 0; i < strs.length; i++) {
            String word = strs[i];
            String rearrangedWord = rearrangeString(word);
            

            List<String> group =
                check.computeIfAbsent(rearrangedWord, k -> new ArrayList<>());

            group.add(word);
        }

        return new ArrayList<>(check.values());
    }

    public String rearrangeString(String input) {
        char[] charArray = input.toCharArray();
        Arrays.sort(charArray);

        return new String(charArray);
    }
}