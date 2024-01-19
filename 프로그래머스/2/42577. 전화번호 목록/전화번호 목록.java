import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book); // 앞 문자부터 숫자의 순서를 기반으로 오름차순 정렬

        for (int i=0; i< phone_book.length-1; i++) {
            if (phone_book[i+1].startsWith(phone_book[i])) {
                    return false;
            }
        }

        return true;
    }
}