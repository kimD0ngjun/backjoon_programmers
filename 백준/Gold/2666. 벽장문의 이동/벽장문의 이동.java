import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // 입력 처리
        int N = Integer.parseInt(br.readLine());
        String[] openCases = br.readLine().split(" ");

        int openA = Integer.parseInt(openCases[0]);
        int openB = Integer.parseInt(openCases[1]);

        int[] targets = new int[Integer.parseInt(br.readLine())];

        for (int i = 0; i < targets.length; i++) {
            targets[i] = Integer.parseInt(br.readLine());
        }

        // 연산
        Recursion recursion = new Recursion(N, openA, openB, targets);
        int answer = recursion.calculate();

        // 출력
        bw.write(String.valueOf(answer));

        // 리소스 해제
        br.close();
        bw.close();
    }
}

class Recursion {
    private final int openA;
    private final int openB;
    private final int[] targets;
    private final Integer[][][] memo;

    public Recursion(int doors, int openA, int openB, int[] targets) {
        this.openA = openA;
        this.openB = openB;
        this.targets = targets;
        this.memo = new Integer[targets.length + 1][doors + 1][doors + 1]; // 메모이제이션 초기화
    }

    // 재귀 수행 메소드
    public int calculate() {
        return this.recursion(0, this.openA, this.openB);
    }

    // 재귀 연산 메소드
    private int recursion(int i, int openA, int openB) {

        // 탈출 조건
        if (i == this.targets.length) return 0;

        // 순서 할당
        int target = this.targets[i];

        // 메모이제이션
        if (this.memo[i][openA][openB] != null) return this.memo[i][openA][openB];

        this.memo[i][openA][openB] = Math.min(
                Math.abs(target - openA) + this.recursion(i + 1, target, openB),
                Math.abs(target - openB) + this.recursion(i + 1, openA, target)
        );

        return this.memo[i][openA][openB];
    }
}