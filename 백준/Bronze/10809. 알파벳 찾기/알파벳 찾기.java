import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        int index = 0;
        
        for (int i = 0; i < 26; i++) {
            list.add(-1);
        }
        
        String s = scanner.nextLine();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int ascii = (int) c - 97; // a = 0, b = 1...
            if (list.get(ascii) == -1) {
                list.set(ascii, index);
            }
            
            index++;
        }
        
        for (int item : list) {
            System.out.print(item + " ");
        }
        scanner.close();
    }
}