import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> set = new HashSet<>();
        int size = 0;

        for (int i=0; i<phone_book.length; i++) {
            set.add(phone_book[i]);
        }

        for (int i=0; i<phone_book.length; i++) {
            for (int j=0; j<phone_book[i].length(); j++) {
                if(set.contains(phone_book[i].substring(0,j))) {
                    return false;
                }
            }
        }

        return true;
    }
}