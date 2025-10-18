import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String strN = br.readLine();
        String strA = br.readLine();

        int N = Integer.parseInt(strN);
        int[] A = Arrays.stream(strA.split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] memo = new int[A.length];
        int pointer = 0; // memo pointer

        for (int el: A) {
            int low = 0;
            int high = pointer - 1;

            while (low <= high) {
                int mid = (low + high) / 2;

                if (memo[mid] < el) low = mid + 1;
                else high = mid - 1;
            }

            if (low >= pointer) {
                memo[pointer] = el;
                pointer++;
            } else {
                memo[low] = el;
            }
        }

        System.out.println(pointer);
        br.close();
    }
}
