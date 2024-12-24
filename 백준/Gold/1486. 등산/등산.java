import java.io.*;
import java.util.*;

public class Main {
    private static final int INF = Integer.MAX_VALUE;

    private static int N;
    private static int M;
    private static int T;
    private static int D;
    private static int[][] mountain;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        mountain = new int[N][M];

        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            mountain[i] = substitute(input);
        }

//        System.out.println("산 구조 : " + Arrays.deepToString(mountain));

        // 등산 최단경로와 하산 최단경로가 다름
        int[][] ascendTime = dijkstraAscend();
        int[][] descendTime = dijkstraDescend();

        int result = -1;

        // int 범위를 넘어서는 합산(닿지 못하는 봉우리 계산)을 위해 long 강제 캐스팅
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                long ascend = ascendTime[i][j];
                long descend = descendTime[i][j];

                if (ascend + descend <= (long) D) {
                    result = Math.max(result, mountain[i][j]);
                }
            }
        }

        System.out.println(result);
        br.close();
    }

    static int[] substitute(String input) {
        int[] mountainLine = new int[M];
        char[] charLine = input.toCharArray();

        for (int i = 0; i < M; i++) {
            if (Character.isUpperCase(charLine[i])) {
                int height = (int) charLine[i] - 65;
                mountainLine[i] = height;
            } else if (Character.isLowerCase(charLine[i])) {
                int height = (int) charLine[i] - 71;
                mountainLine[i] = height;
            }
        }

        return mountainLine;
    }

    static int[][] dijkstraAscend() {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        // 최단 시간 배열 초기화
        int[][] minTime = new int[N][M];
        for (int i = 0; i < N; i++) {
            Arrays.fill(minTime[i], INF);
        }
        minTime[0][0] = 0;

        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(0, 0, 0));

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            int curTime = current.time;
            int x = current.x;
            int y = current.y;

            // 이미 더 짧은 시간이 기록된 경우 스킵
            if (curTime > minTime[x][y]) continue;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 맵 벗어나면 아웃
                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

                int heightDiff = mountain[nx][ny] - mountain[x][y];
                if (Math.abs(heightDiff) > T) continue; // T 초과 시 이동 불가

                int moveTime = heightDiff > 0 ? heightDiff * heightDiff : 1;
                int newTime = curTime + moveTime;

                if (newTime < minTime[nx][ny]) {
                    minTime[nx][ny] = newTime;
                    queue.offer(new Node(nx, ny, newTime));
                }
            }

        }

//        System.out.println("등산 : " + Arrays.deepToString(minTime));
        return minTime;
    }

    static int[][] dijkstraDescend() {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        int[][] minTime = new int[N][M];
        for (int i = 0; i < N; i++) {
            Arrays.fill(minTime[i], INF);
        }
        minTime[0][0] = 0;

        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(0, 0, 0));

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            int curTime = current.time;
            int x = current.x;
            int y = current.y;

            if (curTime > minTime[x][y]) continue;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                // 맵 벗어나면 아웃
                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

                int heightDiff = mountain[x][y] - mountain[nx][ny];
                if (Math.abs(heightDiff) > T) continue; // T 초과 시 이동 불가

                int moveTime = heightDiff <= 0 ? 1 : heightDiff * heightDiff;
                int newTime = curTime + moveTime;

                if (newTime < minTime[nx][ny]) {
                    minTime[nx][ny] = newTime;
                    queue.offer(new Node(nx, ny, newTime));
                }
            }

        }

//        System.out.println("하산 : " + Arrays.deepToString(minTime));
        return minTime;
    }
}

class Node implements Comparable<Node> {
    int x, y, time;

    public Node(int x, int y, int time) {
        this.x = x;
        this.y = y;
        this.time = time;
    }

    @Override
    public int compareTo(Node other) {
        return Integer.compare(this.time, other.time);
    }
}