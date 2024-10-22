import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static int M;
    private static int N;
    private static int[][] map;
    private static int[][] memo;
    private static int[] dx = {-1, 0, 1, 0};
    private static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String size = reader.readLine();
        String[] parts = size.split(" ");
        M = Integer.parseInt(parts[0]);
        N = Integer.parseInt(parts[1]);

        map = new int[M + 1][N + 1];
        memo = new int[M + 1][N + 1];

        for (int i = 1; i < M + 1; i++) {
            String input = reader.readLine();
            String[] inputArray = input.split(" ");

            for (int j = 1; j < N + 1; j++) {
                map[i][j] = Integer.parseInt(inputArray[j - 1]);
                memo[i][j] = -1;
            }
        }

//        System.out.println(Arrays.deepToString(map));
//        System.out.println(Arrays.deepToString(memo));

        System.out.println(dfs(1, 1));
    }

    /**
     * 메모이제이션 + dfs
     * @param x: x좌표
     * @param y: y좌표
     * @return: 해당 좌표까지의 경우의 수
     */
    private static int dfs(int x, int y) {

        if (x == M && y == N) {
            return 1;
        }

        // 이미 방문한 케이스
        if (memo[x][y] != -1) {
            return memo[x][y];
        }
        // 방문하지 않은 케이스
        else {
            // 초기화
            memo[x][y] = 0;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // map out
                if (nx < 1 || ny < 1 || nx > M || ny > N) {
                    continue;
                }

                if (map[x][y] > map[nx][ny]) {
                    memo[x][y] += dfs(nx, ny);
                }
            }
        }

        return memo[x][y];
    }
}