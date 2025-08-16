import java.io.*;
import java.util.*;

public class Main {
    // 도착점, 비용, 소요시간(*)
    static class Node {
        int destination;
        int cost;
        int time;

        Node(int destination, int cost, int time) {
            this.destination = destination;
            this.cost = cost;
            this.time = time;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 얜 왜 있는거야
        String T = br.readLine();

        // 노드 수, 최대 비용, 간선 수
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 그래프 생성
        List<Node>[] routes = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) {
            routes[i] = new ArrayList<>();
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            routes[s].add(new Node(e, w, t));
        }

        // 각 노드별 간선 소요 시간 기준 정렬
        for (int i = 1; i <= N; i++) {
            routes[i].sort(Comparator.comparingInt(a -> a.time));
        }

        bfs(routes, N, M);
    }

    static void bfs(List<Node>[] routes, int N, int M) {
        int INF = Integer.MAX_VALUE;
        // 갱신 배열
        int[][] minTimes = new int[N + 1][M + 1];
        for (int i = 1; i <= N; i++) {
            Arrays.fill(minTimes[i], INF);
        }
        minTimes[1][0] = 0;

        int endMinTime = INF;
        
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 1, 0}); // 현재 시간(*), 현재 노드, 현재 비용

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int curTime = cur[0];
            int curNode = cur[1];
            int curCost = cur[2];

            if (curNode == N && curTime < endMinTime) {
                endMinTime = curTime;
                continue;
            }

            if (routes[curNode].isEmpty()) continue;
            if (minTimes[curNode][curCost] < curTime) continue;

            for (Node node : routes[curNode]) {
                int nextNode = node.destination;
                int nextCost = curCost + node.cost;
                int nextTime = curTime + node.time;

                if (nextCost > M) continue;

                if (nextTime < minTimes[nextNode][nextCost]) {
                    minTimes[nextNode][nextCost] = nextTime;
                    queue.add(new int[]{nextTime, nextNode, nextCost});

                    // 비용 전파
                    for (int c = nextCost + 1; c <= M; c++) {
                        if (minTimes[nextNode][c] <= nextTime) break;
                        minTimes[nextNode][c] = nextTime;
                    }
                }
            }
        }

        if (endMinTime == INF) {
            System.out.println("Poor KCM");
        } else {
            System.out.println(endMinTime);
        }
    }
}
