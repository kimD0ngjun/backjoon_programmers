import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int answer = 0;

        // N의 비트 : 1의 개수 -> 같은 것들끼리 합치고 남은 물병
        // ex) 7일 경우 111. 7 -> 2, 2, 2, 1 -> 4, 2, 1 -> 최종 3개
        while(Integer.bitCount(N) > K) {
            N++;
            answer++; // 1L 물병 구매, N도 그만큼 가산
        }

//        if (answer == 0) answer = -1; // exception

        System.out.println(answer);
    }
}